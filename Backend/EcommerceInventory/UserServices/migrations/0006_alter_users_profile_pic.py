# Generated by Django 5.0.7 on 2024-07-31 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserServices', '0005_alter_users_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile_pic',
            field=models.JSONField(),
        ),
    ]
