# Generated by Django 4.0.4 on 2023-01-10 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productpimagemodel_product'),
        ('account', '0006_accoutusercartproduct_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='accoutUserCartProduct',
            new_name='accountUserCartProduct',
        ),
    ]
