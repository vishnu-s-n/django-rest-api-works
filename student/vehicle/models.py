from django.db import models
from vehicle.utils import statusEnumType,statusVehicleEnumType,statusVehicleAssignEnumType
from accounts.models import accountsUserModel


# Create your models here.
class vehicleVMainModel(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    vehicle_number=models.CharField(max_length=100)
    status = models.CharField(max_length=120, choices=statusEnumType.choices())

class vehicleBreakDownModel(models.Model):
    vehicle=models.ForeignKey(vehicleVMainModel,on_delete=models.CASCADE,related_name="vehicleBreakDownModel_vehicle")
    reason=models.CharField(max_length=100)

class vehicleBreakDownImageModel(models.Model):
    break_down=models.ForeignKey(vehicleBreakDownModel,on_delete=models.CASCADE,related_name="vehicleBreakDownImageModel_break_down")
    image = models.ImageField(upload_to="images", null=True)
    status = models.CharField(max_length=120, choices=statusVehicleEnumType.choices())

class vehicleInspectionModel(models.Model):
    break_down=models.ForeignKey(vehicleBreakDownModel,on_delete=models.CASCADE,related_name="vehicleInspectionModel_break_down")
    reason=models.CharField(max_length=150)

class vehicleAssignModel(models.Model):
    vehicle=models.OneToOneField(vehicleVMainModel,on_delete=models.CASCADE,related_name="vehicleAssignModel_vehicle")
    owner=models.ForeignKey(accountsUserModel,on_delete=models.CASCADE,related_name="vehicleAssignModel_owner")
    status = models.CharField(max_length=120, choices=statusVehicleAssignEnumType.choices())

