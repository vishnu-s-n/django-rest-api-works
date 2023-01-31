from django.contrib import admin
from vehicle.models import *
# Register your models here.

admin.site.register(vehicleVMainModel)
admin.site.register(vehicleBreakDownModel)
admin.site.register(vehicleBreakDownImageModel)
admin.site.register(vehicleAssignModel)
admin.site.register(vehicleInspectionModel)