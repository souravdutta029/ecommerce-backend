# Generated by Django 5.0.7 on 2024-07-29 04:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('InventoryServices', '0002_initial'),
        ('OrderServices', '0001_initial'),
        ('ProductServices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='approved_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_by_user_id_purchase_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='cancelled_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cancelled_by_user_id_purchase_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='created_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_user_id_purchase_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_purchase_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='last_updated_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_updated_by_user_id_purchase_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='received_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_by_user_id_purchase_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='returned_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='returned_by_user_id_purchase_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='supplier_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_id_purchase_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='updated_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_user_id_purchase_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='warehouse_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_id_purchase_order', to='InventoryServices.warehouse'),
        ),
        migrations.AddField(
            model_name='purchaseorderinwardedlogs',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_purchase_order_inwarded_logs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorderinwardedlogs',
            name='inwarded_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inwarded_by_user_id_inwarded_logs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorderinwardedlogs',
            name='po_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='po_id_purchase_order_inwarded_logs', to='OrderServices.purchaseorder'),
        ),
        migrations.AddField(
            model_name='purchaseorderitems',
            name='approved_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_by_user_id_purchase_order_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorderitems',
            name='cancelled_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cancelled_by_user_id_purchase_order_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorderitems',
            name='created_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_user_id_purchase_order_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorderitems',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_purchase_order_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorderitems',
            name='po_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='po_id_purchase_order_items', to='OrderServices.purchaseorder'),
        ),
        migrations.AddField(
            model_name='purchaseorderitems',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_id_purchase_order_items', to='ProductServices.products'),
        ),
        migrations.AddField(
            model_name='purchaseorderitems',
            name='received_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_by_user_id_purchase_order_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorderitems',
            name='returned_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='returned_by_user_id_purchase_order_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorderitems',
            name='updated_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_user_id_purchase_order_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorderiteminwardedlogs',
            name='po_item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='po_item_id_purchase_order_inwarded_logs', to='OrderServices.purchaseorderitems'),
        ),
        migrations.AddField(
            model_name='purchaseorderlogs',
            name='created_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_user_id_purchase_order_logs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorderlogs',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_purchase_order_logs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorderlogs',
            name='po_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='po_id_purchase_order_logs', to='OrderServices.purchaseorder'),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='approved_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_by_user_id_sales_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='cancelled_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cancelled_by_user_id_sales_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='created_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_user_id_sales_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='customer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_id_sales_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_sales_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='last_updated_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_updated_by_user_id_sales_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='received_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_by_user_id_sales_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='returned_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='returned_by_user_id_sales_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='updated_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_user_id_sales_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorderitems',
            name='approved_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_by_user_id_sales_order_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorderitems',
            name='cancelled_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cancelled_by_user_id_sales_order_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorderitems',
            name='created_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_user_id_sales_order_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorderitems',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_sales_order_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorderitems',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_id_so_sales_order_items', to='ProductServices.products'),
        ),
        migrations.AddField(
            model_name='salesorderitems',
            name='returned_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='returned_by_user_id_sales_order_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorderitems',
            name='shipped_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipped_by_user_id_sales_order_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorderitems',
            name='so_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='so_id_sales_order_items', to='OrderServices.salesorder'),
        ),
        migrations.AddField(
            model_name='salesorderitems',
            name='updated_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_user_id_sales_order_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorderitemoutwardedlogs',
            name='so_item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='so_item_id_sales_order_items_outwarded_logs', to='OrderServices.salesorderitems'),
        ),
        migrations.AddField(
            model_name='salesorderlogs',
            name='created_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_user_id_sales_order_logs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorderlogs',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_sales_order_logs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorderlogs',
            name='so_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='so_id_sales_order_logs', to='OrderServices.salesorder'),
        ),
        migrations.AddField(
            model_name='salesorderoutwardedlogs',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_sales_order_outwarded_logs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorderoutwardedlogs',
            name='outwarded_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outwarded_by_user_id_sales_order_outwarded_logs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorderoutwardedlogs',
            name='so_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='so_order_id_sales_order_outwarded_logs', to='OrderServices.salesorder'),
        ),
    ]
