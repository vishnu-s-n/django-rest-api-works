from django.urls import path
from .views import productPCreateView,productGetAllPAPIView,productAddingPProductCartView,productGetCartDetailsPView

urlpatterns = [
    path('product-creation/', productPCreateView.as_view(),name="productCreationAPIViewURL"),
    path('product-all/', productGetAllPAPIView.as_view(), name="productDetailsAPIViewURL"),
    path('product-adding/', productAddingPProductCartView().as_view(), name="productAddingCartAPIViewURL"),
    path('cart-items/',productGetCartDetailsPView.as_view(),name="productGetCartDetailsPViewURL")
]