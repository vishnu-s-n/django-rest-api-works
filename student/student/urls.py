from django.urls import path, include
# from .views import

urlpatterns = [
    path('apis/v1/admin/', include("student.api_v1_admin.urls")),
]
