from rest_framework import serializers
from .models import Cocktail, Collection, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', "fullName", 'userName', "password", 'email', "phone_number"]


class CocktailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'collection', 'ingredients', 'preparation', 'garnish']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name']
