from django.contrib import admin
from django.urls import path, include
from UserServices.Controller.DynamicFormController import DynamicFormController
from UserServices.Controller.SuperAdminDynamicFormController import SuperAdminDynamicFormController
from UserServices.Controller.SidebarController import ModuleView
from EcommerceInventory import settings
from django.conf.urls.static import static
from django.urls import re_path
from EcommerceInventory.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('UserServices.urls')),
    path('api/getForm/<str:modelName>/', DynamicFormController.as_view(), name='dynamicForm'),
    path('api/superAdminForm/<str:modelName>/', SuperAdminDynamicFormController.as_view(), name='superadmindynamicform'),
    path('api/getMenus/', ModuleView.as_view(), name='sidebarmenu'),
    path('api/products/', include('ProductServices.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
urlpatterns += [
    re_path(r'^(?:.*)/?$', index, name='index'),
]
