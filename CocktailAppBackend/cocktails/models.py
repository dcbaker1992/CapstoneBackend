from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=50)


class Cocktail(models.Model):
    name = models.CharField(max_length=50)
    collection = models.ForeignKey(Collection, null=True, on_delete=models.CASCADE)
    ingredients = models.CharField(max_length=250, null=True)
    preparation = models.TextField(null=True)
    garnish = models.CharField(max_length=50, null=True)
