# Generated by Django 4.0.4 on 2023-01-07 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productpimagemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpimagemodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productPImageModel_product', to='product.productpmainmodel'),
        ),
    ]