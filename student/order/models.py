from django.db import models
from account.models import accountUserModel,accountUserCartProduct
from account.utils import statusEnumType


# Create your models here.

class orderOMainModel(models.Model):
    owner=models.ForeignKey(accountUserModel,on_delete=models.CASCADE,related_name="orderOMainModel_owner")
    product=models.ManyToManyField(accountUserCartProduct,related_name="orderOMainModel_product")
    final_price = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=120, choices=statusEnumType.choices())


