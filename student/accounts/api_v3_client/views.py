from rest_framework.response import Response
from  rest_framework.views import APIView
from accounts.models import accountsUserModel,accountsUserProfileModel
from accounts.api_v3_client.serializers import accountsUserCreateSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND,HTTP_200_OK

class accountsCreateAUserView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = accountsUserCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Account Created Successfully"},status=HTTP_200_OK)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
