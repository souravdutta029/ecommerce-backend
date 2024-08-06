from django.db import models
from UserServices.models import Users
from ProductServices.models import Products

# Create your models here.
class PurchaseOrder(models.Model):
    id = models.AutoField(primary_key=True)
    warehouse_id = models.ForeignKey('InventoryServices.Warehouse', on_delete=models.CASCADE, null=True, blank=True, related_name='warehouse_id_purchase_order')
    supplier_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='supplier_id_purchase_order')
    last_updated_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='last_updated_by_user_id_purchase_order')
    po_code = models.CharField(max_length=255)
    po_date = models.DateField()
    expected_delivery_date = models.DateField()
    payment_term = models.CharField(max_length=255, choices=(('COD', 'COD'),('Prepaid', 'Prepaid'), ('Cash', 'Cash'), ('Credit', 'Credit'), ('Online', 'Online'), ('Cheque', 'Cheque')), default='Cash')
    payment_status = models.CharField(max_length=255, choices=(('Pending', 'Pending'),('Paid', 'Paid'),('Unpaid', 'Unpaid'), ('Partially Paid', 'Partially Paid'), ('Cancelled', 'Cancelled')), default='Unpaid')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type = models.CharField(max_length=255, choices=(('Amount', 'Amount'),('Percentage', 'Percentage')), default='Amount')
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_type = models.CharField(max_length=255, choices=(('Free', 'Free'),('Paid', 'Paid')), default='Free')
    shipping_tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    additional_details = models.JSONField()
    status = models.CharField(max_length=255, choices=(('Draft','Draft'), ('Sent','Sent'), ('Received','Received'), ('Cancelled','Cancelled'),('Returned', 'Returned')), default='Draft')
    created_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='created_by_user_id_purchase_order')
    updated_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_by_user_id_purchase_order')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_purchase_order')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='approved_by_user_id_purchase_order')
    approved_at = models.DateTimeField(auto_now_add=True)
    cancelled_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='cancelled_by_user_id_purchase_order')
    cancelled_at = models.DateTimeField(auto_now_add=True)
    cancelled_reason = models.TextField()
    received_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='received_by_user_id_purchase_order')
    received_at = models.DateTimeField(auto_now_add=True)
    returned_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='returned_by_user_id_purchase_order')
    returned_at = models.DateTimeField(auto_now_add=True)
    
    
class PurchaseOrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    po_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, null=True, blank=True, related_name='po_id_purchase_order_items')
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True, related_name='product_id_purchase_order_items')
    quantity_ordered = models.IntegerField()
    quantity_received = models.IntegerField()
    quantity_cancelled = models.IntegerField()
    quantity_returned = models.IntegerField()
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    amount_returned = models.DecimalField(max_digits=10, decimal_places=2)
    amount_cancelled = models.DecimalField(max_digits=10, decimal_places=2)
    amount_ordered = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type = models.CharField(max_length=255, choices=(('Amount', 'Amount'),('Percentage', 'Percentage')), default='Amount')
    additional_details = models.JSONField()
    status = models.CharField(max_length=255, choices=(('Draft','Draft'), ('Sent','Sent'), ('Received','Received'), ('Cancelled','Cancelled'), ('Returned', 'Returned')), default='Draft') 
    created_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='created_by_user_id_purchase_order_items')
    updated_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_by_user_id_purchase_order_items')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_purchase_order_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='approved_by_user_id_purchase_order_items')
    approved_at = models.DateTimeField(auto_now_add=True)
    cancelled_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='cancelled_by_user_id_purchase_order_items')
    cancelled_at = models.DateTimeField(auto_now_add=True)
    cancelled_reason = models.TextField()
    received_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='received_by_user_id_purchase_order_items')
    received_at = models.DateTimeField(auto_now_add=True)
    returned_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='returned_by_user_id_purchase_order_items')
    returned_at = models.DateTimeField(auto_now_add=True)
    
    
class PurchaseOrderInwardedLogs(models.Model):
    id = models.AutoField(primary_key=True)
    po_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, null=True, blank=True, related_name='po_id_purchase_order_inwarded_logs')
    invoice_path = models.TextField()
    invoice_number = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    inwarded_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='inwarded_by_user_id_inwarded_logs')
    inwarded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=(('Draft','Draft'), ('Sent','Sent'), ('Received','Received'), ('Cancelled','Cancelled'), ('Returned', 'Returned')), default='Draft') 
    additional_details = models.JSONField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_purchase_order_inwarded_logs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class PurchaseOrderItemInwardedLogs(models.Model):
    id = models.AutoField(primary_key=True)
    po_item_id = models.ForeignKey(PurchaseOrderItems, on_delete=models.CASCADE, null=True, blank=True, related_name='po_item_id_purchase_order_inwarded_logs')
    inwarded_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type = models.CharField(max_length=255, choices=(('Amount', 'Amount'),('Percentage', 'Percentage')), default='Amount')
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    additional_details = models.JSONField()
    status = models.CharField(max_length=255, choices=(('Draft','Draft'), ('Sent','Sent'), ('Received','Received'), ('Cancelled','Cancelled'), ('Returned','Returned')), default='Draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class PurchaseOrderLogs(models.Model):
    id = models.AutoField(primary_key=True)
    po_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, null=True, blank=True, related_name='po_id_purchase_order_logs')
    comment = models.TextField()
    created_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='created_by_user_id_purchase_order_logs')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_purchase_order_logs')
    additional_details = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
# Sales Order
class SalesOrder(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='customer_id_sales_order')
    last_updated_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='last_updated_by_user_id_sales_order')
    so_code = models.CharField(max_length=255)
    so_date = models.DateField()
    expected_delivery_date = models.DateField()
    payment_term = models.CharField(max_length=255, choices=(('COD', 'COD'),('Prepaid', 'Prepaid'), ('Cash', 'Cash'), ('Credit', 'Credit'), ('Online', 'Online'), ('Cheque', 'Cheque')), default='Cash')
    payment_status = models.CharField(max_length=255, choices=(('Pending', 'Pending'),('Paid', 'Paid'),('Unpaid', 'Unpaid'), ('Partially Paid', 'Partially Paid'), ('Cancelled', 'Cancelled')), default='Unpaid')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type = models.CharField(max_length=255, choices=(('Amount', 'Amount'),('Percentage', 'Percentage')), default='Amount')
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_type = models.CharField(max_length=255, choices=(('Free', 'Free'),('Paid', 'Paid')), default='Free')
    shipping_tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    additional_details = models.JSONField()
    status = models.CharField(max_length=255, choices=(('Draft','Draft'), ('Sent','Sent'), ('Delivered','Delivered'), ('Cancelled','Cancelled'),('Returned', 'Returned')), default='Draft')
    created_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='created_by_user_id_sales_order')
    updated_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_by_user_id_sales_order')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_sales_order')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='approved_by_user_id_sales_order')
    approved_at = models.DateTimeField(auto_now_add=True)
    cancelled_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='cancelled_by_user_id_sales_order')
    cancelled_at = models.DateTimeField(auto_now_add=True)
    cancelled_reason = models.TextField()
    received_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='received_by_user_id_sales_order')
    received_at = models.DateTimeField(auto_now_add=True)
    returned_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='returned_by_user_id_sales_order')
    returned_at = models.DateTimeField(auto_now_add=True)
    
    
class SalesOrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    so_id = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, null=True, blank=True, related_name='so_id_sales_order_items')
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True, related_name='product_id_so_sales_order_items')
    quantity_ordered = models.IntegerField()
    quantity_delivered = models.IntegerField()
    quantity_shipped = models.IntegerField()
    quantity_cancelled = models.IntegerField()
    quantity_returned = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    amount_returned = models.DecimalField(max_digits=10, decimal_places=2)
    amount_cancelled = models.DecimalField(max_digits=10, decimal_places=2)
    amount_ordered = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cancelled_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type = models.CharField(max_length=255, choices=(('Amount', 'Amount'),('Percentage', 'Percentage')), default='Amount')
    additional_details = models.JSONField()
    status = models.CharField(max_length=255, choices=(('Draft','Draft'), ('Sent','Sent'), ('Delivered','Delivered'), ('Cancelled','Cancelled'), ('Returned', 'Returned')), default='Draft') 
    created_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='created_by_user_id_sales_order_items')
    updated_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_by_user_id_sales_order_items')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_sales_order_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='approved_by_user_id_sales_order_items')
    approved_at = models.DateTimeField(auto_now_add=True)
    cancelled_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='cancelled_by_user_id_sales_order_items')
    cancelled_at = models.DateTimeField(auto_now_add=True)
    cancelled_reason = models.TextField()
    shipped_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='shipped_by_user_id_sales_order_items')
    shipped_at = models.DateTimeField(auto_now_add=True)
    returned_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='returned_by_user_id_sales_order_items')
    returned_at = models.DateTimeField(auto_now_add=True)
    
    
class SalesOrderOutwardedLogs(models.Model):
    id = models.AutoField(primary_key=True)
    so_id = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, null=True, blank=True, related_name='so_order_id_sales_order_outwarded_logs')
    invoice_path = models.TextField()
    invoice_number = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    outwarded_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='outwarded_by_user_id_sales_order_outwarded_logs')
    outwarded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=(('Draft','Draft'), ('Sent','Sent'), ('Delivered','Delivered'), ('Cancelled','Cancelled'), ('Returned', 'Returned')), default='Draft') 
    additional_details = models.JSONField()
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_sales_order_outwarded_logs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class SalesOrderItemOutwardedLogs(models.Model):
    id = models.AutoField(primary_key=True)
    so_item_id = models.ForeignKey(SalesOrderItems, on_delete=models.CASCADE, null=True, blank=True, related_name='so_item_id_sales_order_items_outwarded_logs')
    outwarded_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type = models.CharField(max_length=255, choices=(('Amount', 'Amount'),('Percentage', 'Percentage')), default='Amount')
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    additional_details = models.JSONField()
    status = models.CharField(max_length=255, choices=(('Draft','Draft'), ('Sent','Sent'), ('Delivered','Delivered'), ('Cancelled','Cancelled'), ('Returned','Returned')), default='Draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class SalesOrderLogs(models.Model):
    id = models.AutoField(primary_key=True)
    so_id = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, null=True, blank=True, related_name='so_id_sales_order_logs')
    comment = models.TextField()
    created_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='created_by_user_id_sales_order_logs')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='domain_user_id_sales_order_logs')
    additional_details = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    