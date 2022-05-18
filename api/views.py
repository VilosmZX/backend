from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from http import HTTPStatus
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserReg
from .serializers import UserRegSerializer

@api_view(['POST'])
def reg(request: HttpRequest):
    data = request.data
    serializer = UserRegSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        serializer.data['qrcode_url'] = f'localhost:8000/check/{serializer.data["id"]}'
        return Response(serializer.data, status=HTTPStatus.CREATED)
    return Response(status=HTTPStatus.BAD_REQUEST)


@api_view(['GET'])
def check(request: HttpRequest, id):
    try:
        user = UserReg.objects.get(id=id)
        user.delete()
        return Response('Jemaat Terdaftar!',status=200)
    except:
        return Response('Jemaat tidak terdaftar!',status=200)


@api_view(['GET'])
def check_available(request: HttpRequest):
    totalAvailable = UserReg.objects.filter(jam='Jam 8').count()
    totalAvailable = 16 - totalAvailable
    
    if totalAvailable <= 0:
        return Response(0,status=HTTPStatus.BAD_REQUEST)
    return Response({'data': totalAvailable} ,status=200)


@api_view(['GET'])
def check_available2(request: HttpRequest):
    totalAvailable = UserReg.objects.filter(jam='Jam 10').count()
    totalAvailable = 16 - totalAvailable
    if totalAvailable <= 0:
        return Response(0, status=HTTPStatus.BAD_REQUEST)
    return Response({'data': totalAvailable}, status=200)


@api_view(['GET'])
def is_exists(request: HttpRequest, id):
    try:
        user = UserReg.objects.get(id=id)
        return Response(status=200)
    except:
        return Response(status=HTTPStatus.NOT_FOUND)

