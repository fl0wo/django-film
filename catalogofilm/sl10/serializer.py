from rest_framework import serializers
from . models import Film,Categoria

class FilmSerializer(serializers.ModelSerializer) :

    categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='tipo'
     )

    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

    languages = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

    immages = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='img'
     )

    class Meta :
        model = Film
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer) :

    class Meta :
        model = Categoria
        fields = '__all__'