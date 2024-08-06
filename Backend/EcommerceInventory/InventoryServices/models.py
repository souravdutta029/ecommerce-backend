from django.db import models
from UserServices.models import Users
from ProductServices.models import Products
from OrderServices.models import *


# Create your models here.
class Warehouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255)
    warehouse_manager = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='warehouse_manager_id')
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    status = models.CharField(max_length=255, choices=(('Active', 'Active'),('Inactive', 'Inactive'),('Deleted', 'Deleted')), default='Active')
    size = models.CharField(max_length=255, choices=(('Small', 'Small'),('Medium', 'Medium'),('Large', 'Large')), default='Small')
    capacity = models.CharField(max_length=255, choices=(('Low', 'Low'),('Medium', 'Medium'),('High', 'High')), default='Low')
    warehouse_type = models.CharField(max_length=255, choices=(('Owned', 'Owned'),('Leased', 'Leased')), default='Owned')
    additional_details = models.JSONField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_warehouse')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='added_by_user_id_warehouse')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class RackAndShelvesAndFloors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, blank=True, related_name='warehouse_id_rack_and_shelves_and_floors')
    rack = models.CharField(max_length=255, blank=True, null=True)
    shelf = models.CharField(max_length=255, blank=True, null=True)
    floor = models.CharField(max_length=255, blank=True, null=True)
    additional_details = models.JSONField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_rack_and_shelves_and_floors')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='added_by_user_id_rack_and_shelves_and_floors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_order_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, null=True, blank=True, related_name='purchase_order_id_inventory')
    purchase_order_item_id = models.ForeignKey(PurchaseOrderItems, on_delete=models.CASCADE, null=True, blank=True, related_name='purchase_order_item_id_inventory')
    purchase_order_item_inwarded_id = models.ForeignKey(PurchaseOrderItemInwardedLogs, on_delete=models.CASCADE, null=True, blank=True, related_name='purchase_order_item_inwarded_id_inventory')
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True, related_name='product_id_inventory')
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, blank=True, related_name='warehouse_id_inventory')
    rack_and_shelves_and_floors_id = models.ForeignKey(RackAndShelvesAndFloors, on_delete=models.CASCADE, null=True, blank=True, related_name='rack_and_shelves_and_floors_id_inventory')
    quantity = models.IntegerField()
    mrp = models.CharField(max_length=255, blank=True, null=True)
    batch_number = models.CharField(max_length=255, blank=True, null=True)
    discount_type = models.CharField(max_length=255, choices=(('Amount', 'Amount'),('Percentage', 'Percentage')), default='Amount')
    discount_amount = models.FloatField()
    sr_no = models.CharField(max_length=255, blank=True, null=True)
    mfg_date = models.DateTimeField()
    uom = models.CharField(max_length=255)
    ptr = models.CharField(max_length=255, blank=True, null=True)
    received_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    quantity_inwarded = models.IntegerField()
    buy_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    stock_status = models.CharField(max_length=255, choices=(('In Stock', 'In Stock'),('Out of Stock', 'Out of Stock'), ('Damaged', 'Damaged'), ('Lost', 'Lost')), default='In Stock')
    inward_type = models.CharField(max_length=255, choices=(('Purchase', 'Purchase'),('Return', 'Return'), ('Replacement', 'Replacement'), ('Warehouse Transfer', 'Warehouse Transfer')), default='Purchase')
    additional_details = models.JSONField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_inventory')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='added_by_user_id_inventory')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class InventoryLogs(models.Model):
    id = models.AutoField(primary_key=True)
    po_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, null=True, blank=True, related_name='po_id_inventory_logs')
    so_id = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, null=True, blank=True, related_name='so_id_inventory_logs')
    inventory_id = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True, blank=True, related_name='inventory_id_inventory_logs')
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, blank=True, related_name='warehouse_id_inventory_logs')
    rack_shelves_and_floors_id = models.ForeignKey(RackAndShelvesAndFloors, on_delete=models.CASCADE, null=True, blank=True, related_name='rack_shelves_and_floors_id_inventory_logs')
    quantity = models.IntegerField()
    additional_details = models.JSONField()
    status = models.CharField(max_length=255, choices=(('Inward', 'Inward'),('Outward', 'Outward'), ('Damaged', 'Damaged'), ('Lost', 'Lost'), ('Expired', 'Expired'), ('Returned', 'Returned'), ('Adjusment', 'Adjustment'), ('Warehouse Transfer', 'Warehouse Transfer')), default='Inward')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_inventory_logs')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='added_by_user_id_inventory_logs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)