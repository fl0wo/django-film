from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Film,Categoria
from . serializer import FilmSerializer,CategorySerializer

class FilmList(APIView) : 

    def get(self , request) :
        films1 = Film.objects.all()
        serializer = FilmSerializer(films1,many = True)
        return Response(serializer.data)

    def post(self) :
        pass

class CategoriesList(APIView) : 

    def get(self , request) :
        categoriee = Categoria.objects.all()
        serializer = CategorySerializer(categoriee,many = True)
        return Response(serializer.data)

    def post(self) :
        pass