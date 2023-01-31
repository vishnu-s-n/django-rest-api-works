from rest_framework.response import Response
from rest_framework.views import APIView
from order.models import orderOMainModel
from order.api_v2_client.serializers import orderAddingSerializer

class orderOAPIView(APIView):
    def post(self,request,id,*args,**kwargs):
        user_id=self.kwargs["id"]
        print(user_id)
        serializer = orderAddingSerializer(data=request.data,context={'request': request,'user_id':user_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(data=serializer.errors)