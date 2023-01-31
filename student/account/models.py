from django.db import models
from product.models import productPMainModel
from account.utils import statusEnumType


# Create your models here.

class accountUserModel(models.Model):
    phonenumber = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class accountUserProfileModel(models.Model):
    owner = models.OneToOneField(accountUserModel, on_delete=models.CASCADE,related_name="accountUserProfileModel_owner")
    name = models.CharField(max_length=140)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return self.name


class accountUserCartProduct(models.Model):
    owner = models.ForeignKey(accountUserModel, on_delete=models.CASCADE, related_name="accountUserCartProduct_owner")
    product = models.ForeignKey(productPMainModel, on_delete=models.CASCADE,related_name="accountUserCartProduct_product")
    status = models.CharField(max_length=120, choices=statusEnumType.choices())


class accountUserCartModel(models.Model):
    owner = models.OneToOneField(accountUserModel, on_delete=models.CASCADE, related_name="accountUserCartModel_owner")
    products = models.ManyToManyField(accountUserCartProduct, related_name="accountUserCartModel_products")
    final_price = models.PositiveIntegerField(null=True, blank=True)


class accountUserLoginOtpModel(models.Model):
    owner = models.ForeignKey(accountUserModel, on_delete=models.CASCADE, related_name="accountUserLoginOtpModel_owner")
    otp = models.IntegerField()
    active = models.BooleanField()
