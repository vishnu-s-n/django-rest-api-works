from django.urls import path
from .views import orderOAPIView
urlpatterns = [
    path('order-adding/<int:id>/', orderOAPIView.as_view(), name="orderOAPIViewURL")

]


