from django.urls import path
from .views import vehicleCreateView,vehicleBreakdownView,vehicleAssignView,vehicleInspectionView

urlpatterns = [
    path('vehicle-creation/',vehicleCreateView.as_view(),name="vehicleCreateViewAPIViewURL"),
    path('vehicle-breakdown/',vehicleBreakdownView.as_view(),name="vehicleBreakdownViewAPIViewURL"),
    path('vehicle-assign/',vehicleAssignView.as_view(),name="vehicleAssignViewAPIViewURL"),
    path('vehicle-inspection/',vehicleInspectionView.as_view(),name="vehicleInspectionViewAPIViewURL")
]


