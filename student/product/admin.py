from django.contrib import admin
from product.models import *
# Register your models here.

admin.site.register(productPMainModel)

class productImageAdmin(admin.StackedInline):
    models=productPImageModel

admin.site.register(productPImageModel)