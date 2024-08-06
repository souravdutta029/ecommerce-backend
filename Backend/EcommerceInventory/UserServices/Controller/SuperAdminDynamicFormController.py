from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.apps import apps
from django.core.serializers import serialize
from rest_framework_simplejwt.authentication import JWTAuthentication
from EcommerceInventory.permission import isSuperAdmin
import json
from EcommerceInventory.Helper import renderResponse, getSuperAdminDynamicFormModels, getExcludedFields

class SuperAdminDynamicFormController(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, isSuperAdmin]

    def post(self, request, modelName):
        """
        POST method to create a new instance of a dynamic form model.
        """
        # Check if modelName exists in dynamic form models
        if modelName not in getSuperAdminDynamicFormModels():
            return renderResponse(data = 'Model not exist', message='Model not exist', status=status.HTTP_404_NOT_FOUND)
        
        # Get the model class
        model = getSuperAdminDynamicFormModels()[modelName]
        model_class = apps.get_model(model)
        
        # Check if model class exists
        if model_class is None:
            return renderResponse(data='Model not found', message='Model not found', status=status.HTTP_404_NOT_FOUND)
        
        # Get model fields
        fields_info = model_class._meta.fields
        model_fields = {field.name for field in fields_info}
        excluded_fields = getExcludedFields()
        
        # Get required fields
        required_fields = [field.name for field in fields_info if not field.null and field.default is not None and field.name not in excluded_fields]
        missing_fields = [field for field in required_fields if field not in request.data]
        print(missing_fields)
        
        # Check if all required fields are present
        if missing_fields:
            return renderResponse(data=[f'The Following field in required : {field}' for field in missing_fields], message="Validation error", status=status.HTTP_400_BAD_REQUEST)
        
        # Prepare fields data
        fields = request.data.copy()
        fieldsdata = {key:value for key, value in fields.items() if key in model_fields}
        
        # Assigning foreign key instance for ForeignKey fields
        for field in fields_info:
            if field.is_relation and field.name in fieldsdata and isinstance(fieldsdata[field.name], int):
                related_model = field.related_model
                try:
                    fieldsdata[field.name] = related_model.objects.get(id=fieldsdata[field.name])
                except related_model.DoesNotExist:
                    return renderResponse(data=f'{field.name} Related model does not exist', message=f'{field.name} Related model does not exist', status=status.HTTP_400_BAD_REQUEST)
        
        # Create model instance
        model_instance = model_class.objects.create(**fieldsdata)
        serialized_data = serialize('json', [model_instance])
        model_json = json.loads(serialized_data)
        response_json = model_json[0]['fields']
        response_json['id'] = model_json[0]['pk']
        
        return renderResponse(data = response_json, message='Data saved successfully', status=status.HTTP_201_CREATED)