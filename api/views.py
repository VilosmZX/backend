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
