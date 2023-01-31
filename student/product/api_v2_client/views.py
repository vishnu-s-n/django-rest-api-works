from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import productPImageModel,productPMainModel
from product.api_v2_client.serializers import productPCreateSerializer,productGetAllPSerializer,productAddingCartSerializer,productGetCartDetailsSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND,HTTP_200_OK
from account.models import accountUserCartModel

class productPCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = productPCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Product Create Successfully"},status=HTTP_200_OK)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


class productGetAllPAPIView(APIView,LimitOffsetPagination):
    def get(self,request,*args,**kwargs):
        queryset = productPMainModel.objects.all()
        result = self.paginate_queryset(queryset, request, view=self)
        serializer = productGetAllPSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)



class productAddingPProductCartView(APIView):
    def post(self,request):
        serializer=productAddingCartSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response({"message":"Successfully added to cart"},status=HTTP_200_OK)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

class productGetCartDetailsPView(APIView,LimitOffsetPagination):
    def get(self,request,*args,**kwargs):
        queryset = accountUserCartModel.objects.all()
        result = self.paginate_queryset(queryset, request, view=self)
        serializer =productGetCartDetailsSerializer (result, many=True)
        return self.get_paginated_response(serializer.data)


# class CustomPagination(pagination.LimitOffsetPagination):
#     default_limit = 2
#     limit_query_param = 'l'
#     offset_query_param = 'o'
#     max_limit = 50

# Alternatively, you can just use paginate_queryset and get_paginated_response

# def list(self,request):
#     country_data = Country.objects.all()
#
#     page = self.paginate_queryset(country_data)
#     if page is not None:
#        serializer = self.get_serializer(page, many=True)
#        return self.get_paginated_response(serializer.data)
#
#     serializer = self.get_serializer(country_data, many=True)
#     return Response(serializer.data)