# Generated by Django 4.0.4 on 2023-01-10 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productpimagemodel_product'),
        ('account', '0004_alter_accountusercartmodel_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountusercartmodel',
            name='products',
            field=models.ManyToManyField(related_name='accountUserCartModel_products', to='product.productpmainmodel'),
        ),
        migrations.AlterField(
            model_name='accountuserprofilemodel',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accountUserProfileModel_owner', to='account.accountusermodel'),
        ),
    ]
