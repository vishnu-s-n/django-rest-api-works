from django.contrib import admin
from account.models import *
# Register your models here.

admin.site.register(accountUserModel)
admin.site.register(accountUserCartModel)
admin.site.register(accountUserCartProduct)
admin.site.register(accountUserProfileModel)
admin.site.register(accountUserLoginOtpModel)
