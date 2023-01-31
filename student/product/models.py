from django.db import models
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
import random
import string

# Create your models here.

class productPMainModel(models.Model):
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=200)
    unique_code=models.CharField(max_length=100,unique=True)
    price=models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.title

# @receiver(pre_save,sender=productPMainModel)
# def create_product(sender,instance,**kwargs):
#     print("signal is calling")
#     if not instance.unique_code:
#
#         chars=string.digits
#         a=''.join(random.choice(chars) for _ in range(5))
#         instance.unique_code="#"+a
#         print(instance.unique_code)
#
#
#     # instance.product.save()

def unique_code(sender,instance,*args,**kwargs):
    chars=string.digits
    a= "" .join(random.choice(chars) for _ in range(5))
    instance.unique_code = "#" + a
    print(instance.unique_code)

pre_save.connect(unique_code,sender=productPMainModel)



class productPImageModel(models.Model):
    product=models.ForeignKey(productPMainModel,on_delete=models.CASCADE,related_name="productPImageModel_product")
    image=models.ImageField(upload_to="images",null=True)

