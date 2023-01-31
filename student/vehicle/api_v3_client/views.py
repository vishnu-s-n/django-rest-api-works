from rest_framework.response import Response
from rest_framework.views import APIView
from vehicle.models import vehicleVMainModel
from vehicle.api_v3_client.serializers import vehicleCreationSerializer,vehicleBreakDownSerializer,vehicleAssignSerializer,vehicleInspectionSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_200_OK

class vehicleCreateView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = vehicleCreationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Vehicle Created Successfully"},status=HTTP_200_OK)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

class vehicleAssignView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = vehicleAssignSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Vehicle Assigned Successfully"},status=HTTP_200_OK)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

class vehicleBreakdownView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = vehicleBreakDownSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Break Down Added Successfully"}, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class vehicleInspectionView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = vehicleInspectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Inspection Created Successfully"}, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)




