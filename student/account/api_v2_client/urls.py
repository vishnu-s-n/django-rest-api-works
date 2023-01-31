from django.urls import path
from .views import accountCreateAUserView,accountGetAllAAPIView,accountSendOtpAAPIView,accountLoginAAPIView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('account-creation/', accountCreateAUserView.as_view(),name="accountCreationAPIViewURL"),
    path('account-all/',accountGetAllAAPIView.as_view(),name="accountGetAllAPIViewURL"),
    path('email-otp/',accountSendOtpAAPIView.as_view(),name="accountEmailOtpAPIViewURL"),
    path('account-login/', accountLoginAAPIView.as_view(), name="accountLoginAPIViewURL"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')

]






