from rest_framework.response import Response
from rest_framework.views import APIView
from account.models import accountUserModel,accountUserProfileModel,accountUserCartModel,accountUserCartProduct,accountUserLoginOtpModel
from account.api_v2_client.serializers import accountUserCreateSerializer,accountGetAllASerializer,accountGenarateOtpSerializer,accountLoginSerializer
from .email import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND,HTTP_200_OK


class accountCreateAUserView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = accountUserCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Account Created Successfully"},status=HTTP_200_OK)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


class accountGetAllAAPIView(APIView,LimitOffsetPagination):
    def get(self,request,*args,**kwargs):
        queryset = accountUserProfileModel.objects.all()
        result = self.paginate_queryset(queryset,request,view=self)
        serializer = accountGetAllASerializer(result, many=True)
        return self.get_paginated_response(serializer.data)



class accountSendOtpAAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = accountGenarateOtpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request)
            return Response({"message":"OTP sended to your email"},status=HTTP_200_OK)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


class accountLoginAAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = accountLoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Login Successfull"},status=HTTP_200_OK)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

#
#

# <editor-fold desc="User Login with JWT authentication">
# class accountLoginAAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = accountLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.data["email"]
#             otp = serializer.data["otp"]
#             print(email)
#             print(otp)
#             owner = accountUserModel.objects.get(email=email)
#             user = accountUserLoginOtpModel.objects.filter(owner__email=email,otp=otp)
#             print(user)
#
#             if user.exists():
#                 refresh = RefreshToken.for_user(owner)
#                 return Response(
#                     {
#                         'refresh': str(refresh),
#                         'access': str(refresh.access_token),
#                     }
#                 )
#             else:
#                 return Response({
#                     "msg":"invalid otp"
#                 })
#         else:
#             return Response(
#                 {
#                    "msg" : "Invalid Email or OTP"
#                 }
#             )
# </editor-fold>

# <editor-fold desc="OTP generated ">
# class accountSendOtpAAPIView(APIView):
#     def post(self,request,*args,**kwargs):
#
#             serializer = accountGenarateOtpSerializer(data=request.data)
#             if serializer.is_valid():
#                 email = serializer.data["email"]
#                 accountUserModel.objects.filter(email=email)
#                 send_otp_email(serializer.data['email'])
#                 return Response({
#                     "message":"OTP sended to your email",
#                     "data": serializer.data
#                 })
#             else:
#                 return Response({
#                     "message" : "Inavlid Email"
#                 })
# </editor-fold>


