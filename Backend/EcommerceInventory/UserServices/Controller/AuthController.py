from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from UserServices.models import Users
from EcommerceInventory.Helper import renderResponse
from EcommerceInventory.permission import isSuperAdmin

class SignupAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        profile_pic = request.data.get('profile_pic')
        
        emailCheck = Users.objects.filter(email=email)
        if emailCheck.exists():
            return renderResponse(data = 'Email already exists', message='Email already exists', status=status.HTTP_400_BAD_REQUEST)
        
        usernameCheck = Users.objects.filter(username=username)
        if usernameCheck.exists():
            return renderResponse(data = 'Username already exists', message='Username already exists', status=status.HTTP_400_BAD_REQUEST)
        
        if username is None or email is None or password is None:
            return renderResponse(data = 'Please provide username, email and password', message='Please provide username, email and password', status=status.HTTP_400_BAD_REQUEST)
        
        user = Users.objects.create_user(username=username, email=email, password=password, profile_pic=profile_pic)
        if request.data.get('domain_user_id'):
            user.domain_user_id = Users.objects.get(id=request.data.get('domain_user_id'))
        user.save()
        
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        access['username'] = user.username
        access['email'] = user.email
        access['profile_pic'] = user.profile_pic
        
        return Response({'access': str(access), 'refresh': str(refresh), 'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return renderResponse(data = 'Please provide username and password', message='Please provide username and password', status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            access['username'] = user.username
            access['email'] = user.email
            
            return Response({
                'refresh': str(refresh),
                'access': str(access),
            })
        else:
            return renderResponse(data='Invalid credentials', message='Invalid credentials', status=status.HTTP_401_UNAUTHORIZED)
        
    def get(self, request):
        return renderResponse(data='Please use Post method to login', message='Please use Post method to login', status=status.HTTP_400_BAD_REQUEST)


class PublicAPIView(APIView):
    def get(self, request):
        return renderResponse(data='This is a public API', message='This is a public API', status=status.HTTP_200_OK)
    
class ProtectedAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return renderResponse(data='This is a JWT protected API', message='This is a JWT protected API', status=status.HTTP_200_OK)
    
    
class SuperAdminCheckApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, isSuperAdmin]

    def get(self, request):
        return renderResponse(data='This is SuperAdmin API', message='This is SuperAdmin API', status=status.HTTP_200_OK)
        