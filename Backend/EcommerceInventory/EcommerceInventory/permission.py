from EcommerceInventory.Helper import renderResponse
from rest_framework import status
from rest_framework.permissions import BasePermission

class isSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        if hasattr(request.user, 'role') and request.user.role == 'Super Admin':
            return True
        return False
    
    def __call__(self, request):
        if not self.has_permission(request, None):
            return renderResponse(data='You are not Authorized to access this page', message='You are not Authorized to access this page', status=status.HTTP_401_UNAUTHORIZED)
        return None