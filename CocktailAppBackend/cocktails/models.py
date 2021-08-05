from django.db import models


class User(models.Model):
    fullName = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=True)


class Collection(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class Cocktail(models.Model):
    name = models.CharField(max_length=250)
    collection = models.ForeignKey(Collection, null=True, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    ingredients = models.CharField(max_length=250, null=True)
    preparation = models.TextField(null=True)
    garnish = models.CharField(max_length=50, null=True)
