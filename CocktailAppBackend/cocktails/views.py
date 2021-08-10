from django.shortcuts import render
from .models import Cocktail, Collection, User
from .serializers import CocktailSerializer, CollectionSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class User_list(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):

    def get_users(self):
        users = list(User.objects.all().values())
        return users

    def post(self, request):
        users = self.get_users()

        print(users)
        for user in users:
            print(user)
            print(request.data['userName'])
            if request.data['userName'] == user['userName'] and request.data['password'] == user['password']:
                print("logged in")
                return Response(user)


class CocktailList(APIView):

    def get(self, request):
        cocktail = Cocktail.objects.all()
        serializer = CocktailSerializer(cocktail, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CocktailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class CocktailDetails(APIView):

    def get_cocktail(self, pk):
        try:
            return Cocktail.objects.get(pk=pk)
        except Cocktail.DoesNotExist:
            raise Http404

    def get(self, request, pk, collection_id):
        try:
            cocktail = self.get_cocktail(pk)
            serializer = CocktailSerializer(cocktail)
            return Response(serializer.data)
        except Cocktail.DoesNotExist:
            raise Http404

    def put(self, request, pk, collection_id):
        cocktail = self.get_cocktail(pk)
        serializer = CocktailSerializer(cocktail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, collection_id):
        cocktail = self.get_cocktail(pk)
        cocktail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionList(APIView):

    def get(self, request):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CocktailsInCollection(APIView):

    def get(self, request, collection_id):
        cocktails = Cocktail.objects.filter(collection_id=collection_id)
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)


class CollectionDetails(APIView):

    def get_collection(self, pk):
        try:
            return Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        collection = self.get_collection(pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        collection = self.get_collection(pk)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
