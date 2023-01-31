from django.urls import path
from .views import studentGetAllSAPIView, studentGetSpecificSAPIView, studentPostGradeSAPIView,studentCreateSAPIView

urlpatterns = [
    path('student-all/', studentGetAllSAPIView.as_view(),name="studentGetAllSAPIViewURL"),
    path("student-specific/<int:id>", studentGetSpecificSAPIView.as_view(),name="studentGetSpecificSAPIViewURL"),
    path("student-grade-add/<int:id>",studentPostGradeSAPIView.as_view(),name="studentPostGradeAPIViewURL"),
    path("student-creation/",studentCreateSAPIView.as_view(),name="studentCreationAPIViewURL")
]

