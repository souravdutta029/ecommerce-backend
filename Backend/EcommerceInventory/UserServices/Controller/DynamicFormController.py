from rest_framework.views import APIView
from EcommerceInventory.Helper import getDynamicFormModels, getDynamicFormFields
from rest_framework.response import Response
from django.apps import apps
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from EcommerceInventory.Helper import getExcludedFields, renderResponse
from django.core.serializers import serialize
import json
from UserServices.models import Users
from rest_framework import status

class DynamicFormController(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, modelName):
        """
        POST method to create a new instance of a dynamic form model.
        """
        # Check if modelName exists in dynamic form models
        if modelName not in getDynamicFormModels():
            return renderResponse(data = 'Model not exist', message='Model not exist', status=status.HTTP_404_NOT_FOUND)
        
        # Get the model class
        model = getDynamicFormModels()[modelName]
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
            elif field.is_relation and field.name in fieldsdata:
                fieldsdata.pop(field.name)
        
        # Create model instance
        fieldsdata['domain_user_id'] = request.user.domain_user_id
        fieldsdata['added_by_user_id'] = Users.objects.get(id=request.user.id)
        
        model_instance = model_class.objects.create(**fieldsdata)
        serialized_data = serialize('json', [model_instance])
        model_json = json.loads(serialized_data)
        response_json = model_json[0]['fields']
        response_json['id'] = model_json[0]['pk']
        
        return renderResponse(data = response_json, message='Data saved successfully', status=status.HTTP_201_CREATED)
            
            
    def get(self, request, modelName):
        """
        GET method to get the form fields of a dynamic form model.
        """
        # Check if modelName exists in dynamic form models
        if modelName not in getDynamicFormModels():
            return renderResponse(data='Model not exists', message='Model not exists', status=status.HTTP_404_NOT_FOUND)
        
        # Get the model class
        model = getDynamicFormModels()[modelName]
        model_class = apps.get_model(model)
        
        # Check if model class exists
        if model_class is None:
            return renderResponse(data='Model not found', message='Model not found', status=status.HTTP_404_NOT_FOUND)
        
        # Get model instance
        model_instance = model_class()
        fields = getDynamicFormFields(model_instance, request.user.domain_user_id)
        return renderResponse(data = fields, message='Form fields fetched successfully', status=status.HTTP_200_OK)
