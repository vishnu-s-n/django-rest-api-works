from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import studentSModel,studentMarkModel
from student.api_v1_admin.serializers import studentGetAllSSerializer,studentDetailSerializer,studentMarkSerializer,studentPostGradeSSerializer,studentAdminCreateSerializer
from rest_framework import generics
# Create your views here.

class studentGetAllSAPIView(APIView):
    def get(self,request,*args,**kwargs):
        queryset=studentSModel.objects.all()
        serializer=studentGetAllSSerializer(queryset,many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = studentGetAllSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(data=serializer.errors)

class studentGetSpecificSAPIView(APIView):
    def get(self,request,id,*args,**kwargs):
        queryset=studentSModel.objects.get(id=id)
        serializer=studentDetailSerializer(queryset)
        return Response(data=serializer.data)

class studentPostGradeSAPIView(generics.CreateAPIView):
    queryset = studentMarkModel
    serializer_class = studentPostGradeSSerializer

    def post(self,request,id,*args,**kwargs):
        request.data["owner"]=id
        serializer=studentPostGradeSSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class studentCreateSAPIView(APIView):
    def post(self, request, *args, **kwargs):

        serializer = studentAdminCreateSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(data=serializer.errors)
