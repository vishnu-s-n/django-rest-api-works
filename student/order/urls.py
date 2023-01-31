from django.urls import path, include
# from .views import

urlpatterns = [
    path('apis/v2/client/', include("order.api_v2_client.urls"))
]
