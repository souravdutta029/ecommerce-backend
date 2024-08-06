from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True, choices=(('India', 'India'), ('USA', 'USA'), ('UK', 'UK'), ('Canada', 'Canada'), ('Australia', 'Australia'), ('Japan', 'Japan'), ('France', 'France'), ('Germany', 'Germany'), ('Mexico', 'Mexico'), ('South Korea', 'South Korea'), ('Others', 'Others')))
    profile_pic = models.JSONField(blank=True, null=True)
    account_status = models.CharField(max_length=50, choices=(('Active', 'Active'), ('Inactive', 'Inactive'), ('Suspended', 'Suspended'), ('Deleted', 'Deleted'), ('Blocked', 'Blocked')))
    role = models.CharField(max_length=50, choices=(('User', 'User'), ('Admin', 'Admin'), ('Supplier', 'Supplier'), ('Customer', 'Customer'), ('Staff', 'Staff'), ('Manager', 'Manager'), ('Super Admin', 'Super Admin')))
    dob = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    password = models.CharField(max_length=255)
    social_media_links = models.JSONField(blank=True, null=True)
    additional_details = models.JSONField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True, choices=(('English', 'English'), ('French', 'French'), ('German', 'German'), ('Spanish', 'Spanish'), ('Chinese', 'Chinese'), ('Japanese', 'Japanese'), ('Russian', 'Russian'), ('Arabic', 'Arabic'), ('Portuguese', 'Portuguese'), ('Vietnamese', 'Vietnamese'), ('Hindi', 'Hindi'), ('Korean', 'Korean')))
    department = models.CharField(max_length=50, blank=True, null=True, choices=(('IT', 'IT'), ('HR', 'HR'), ('Marketing', 'Marketing'), ('Finance', 'Finance'), ('Sales', 'Sales'), ('Other', 'Other')))
    designation = models.CharField(max_length=50, blank=True, null=True, choices=(('CEO', 'CEO'), ('CFO', 'CFO'), ('COO', 'COO'), ('CTO', 'CTO'), ('Director', 'Director'),('Manager', 'Manager'), ('Developer', 'Developer'), ('Designer', 'Designer'), ('Accountant', 'Accountant'), ('Sales Representative', 'Sales Representative'), ('Other', 'Other')))
    time_zone = models.CharField(max_length=50, blank=True, null=True, choices=(('UTC-12:00', 'UTC-12:00'), ('UTC-11:00', 'UTC-11:00'), ('UTC-10:00', 'UTC-10:00'),('UTC-09:30', 'UTC-09:30'), ('UTC-09:00', 'UTC-09:00'), ('UTC-08:00', 'UTC-08:00'),('UTC-07:00', 'UTC-07:00'), ('UTC-06:00', 'UTC-06:00'), ('UTC-05:00', 'UTC-05:00'),('UTC-04:00', 'UTC-04:00'), ('UTC-03:30', 'UTC-03:30'), ('UTC-03:00', 'UTC-03:00'),('UTC-02:00', 'UTC-02:00'), ('UTC-01:00', 'UTC-01:00'), ('UTC', 'UTC'), ('UTC+01:00', 'UTC+01:00'),('UTC+02:00', 'UTC+02:00'), ('UTC+03:00', 'UTC+03:00'), ('UTC+03:30', 'UTC+03:30'),('UTC+04:00', 'UTC+04:00'), ('UTC+04:30', 'UTC+04:30'), ('UTC+05:00', 'UTC+05:00'),('UTC+05:30', 'UTC+05:30'), ('UTC+05:45', 'UTC+05:45'), ('UTC+06:00', 'UTC+06:00'),('UTC+06:30', 'UTC+06:30'), ('UTC+07:00', 'UTC+07:00'), ('UTC+08:00', 'UTC+08:00'),('UTC+08:45', 'UTC+08:45'), ('UTC+09:00', 'UTC+09:00'), ('UTC+09:30', 'UTC+09:30'),('UTC+10:00', 'UTC+10:00'), ('UTC+10:30', 'UTC+10:30'), ('UTC+11:00', 'UTC+11:00'),('UTC+12:00', 'UTC+12:00'), ('UTC+12:45', 'UTC+12:45'), ('UTC+13:00', 'UTC+13:00'),('UTC+14:00', 'UTC+14:00')))
    last_login = models.DateTimeField(blank=True, null=True)
    last_device = models.CharField(max_length=50, blank=True, null=True)
    last_ip = models.CharField(max_length=50, blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True, choices=(('USD', 'USD'),('INR', 'INR'),('EUR', 'EUR'),('JPY', 'JPY'),('AUD', 'AUD'),('CAD', 'CAD'),('CNY', 'CNY'),('TRY', 'TRY'),('GBP', 'GBP'),('CHF', 'CHF')))
    domain_user_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    domain_name = models.CharField(max_length=50, blank=True, null=True)
    plan_type = models.CharField(max_length=50, blank=True, null=True, choices=(('Free', 'Free'),('Basic', 'Basic'),('Premium', 'Premium'),('Enterprise', 'Enterprise'),('Standard', 'Standard')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def defaultkey():
        return 'username'
    
    def save(self, *args, **kwargs):
        if not self.domain_user_id and self.id:
            self.domain_user_id = Users.objects.get(id=self.id)
        super().save(*args, **kwargs)
    

class UserShippingAddress(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=50, choices=(('Home', 'Home'), ('Office', 'Office'), ('Other', 'Other')))
    address = models.TextField()
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True, choices=(('India', 'India'), ('USA', 'USA'), ('UK', 'UK'), ('Canada', 'Canada'), ('Australia', 'Australia'), ('Japan', 'Japan'), ('France', 'France'), ('Germany', 'Germany'), ('Mexico', 'Mexico'), ('South Korea', 'South Korea'), ('Others', 'Others')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Modules(models.Model):
    id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=50)
    module_icon = models.CharField(blank=True, null=True, max_length=255)
    is_menu = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    module_url = models.CharField(blank=True, null=True, max_length=255)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    display_order = models.IntegerField(default=0)
    module_description = models.CharField(blank=True, null=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class UserPermissions(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    is_view = models.BooleanField(default=False)
    is_add = models.BooleanField(default=False)
    is_edit = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    domain_user_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class ActivityLog(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    activity = models.TextField()
    activity_type = models.CharField(max_length=50, blank=True, null=True)
    activity_date = models.DateTimeField(auto_now_add=True)
    activity_ip = models.GenericIPAddressField()
    activity_device = models.CharField(max_length=50, blank=True, null=True)
    domain_user_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
