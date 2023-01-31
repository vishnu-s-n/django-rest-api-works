from django.db import models
from student.utils import genderEnumType


# Create your models here.
class accountsUserModel(models.Model):
    phonenumber=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class accountsUserProfileModel(models.Model):
    owner=models.OneToOneField(accountsUserModel,on_delete=models.CASCADE,related_name="accountsUserProfileModel_owner")
    name=models.CharField(max_length=150)
    image=models.ImageField(upload_to="images",null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=120, choices=genderEnumType.choices())


