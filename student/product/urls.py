from django.urls import path, include
# from .views import

urlpatterns = [
    path('apis/v2/client/', include("product.api_v2_client.urls"))
]
