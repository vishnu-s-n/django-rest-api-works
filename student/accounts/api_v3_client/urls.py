from django.urls import path
from .views import accountsCreateAUserView

urlpatterns = [
    path('accounts-creation/', accountsCreateAUserView.as_view(),name="accountsCreationAPIViewURL")

]


