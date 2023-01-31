from django.urls import path, include
# from .views import

urlpatterns = [
    path('apis/v3/client/', include("accounts.api_v3_client.urls"))
]
