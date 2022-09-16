from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
import json
from rest_framework.views import APIView
from pathlib import Path
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def create_and_show_acount(request):
    if request.method=="GET":
        data=Account.objects.all()
        serializer=accountSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = accountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def userData(request,id):
    #try:
    data=Account.objects.get(id=id)
    serializer=accountSerializer(data,context={'request': request})
    return Response(serializer.data)
    #except:
     #   googleData=UserTokens.objects.get(id=id)
      #  serializer=tokenSerializer(googleData,context={'request':request},many=True)       
       # return Response(serializer.data)

@api_view(['PUT'])
def updateData(request,id):
    datas=Account.objects.get(id=id)
    print(request.data)
    serializer=accountSerializer(datas,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)