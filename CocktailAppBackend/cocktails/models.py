from django.db import models


# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)


class Ingredient(models.Model):
    type = models.CharField(max_length=250, unique=True)


class Cocktail(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    preparation = models.TextField(null=True)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)


class Review(models.Model):
    cocktail = models.ForeignKey(Cocktail, blank=True, null=True, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=500)
    rating = models.IntegerField()
    reviewer = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
