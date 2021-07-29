from django.db import models


# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)


class Review(models.Model):
    cocktail_id = models.CharField(max_length=50)
    review_text = models.CharField(max_length=500)
    rating = models.IntegerField(max_length=5)
    reviewer = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)


class FavoritesList(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    cocktail_id = models.CharField(max_length=50)


class Ingredients(models.Model):
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=250)


class CustomDrink(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    ingredient_1 = models.ForeignKey(Ingredients, blank=True, null=True, on_delete=models.CASCADE)
    ingredient_2 = models.ForeignKey(Ingredients, blank=True, null=True, on_delete=models.CASCADE)
    ingredient_3 = models.ForeignKey(Ingredients, blank=True, null=True, on_delete=models.CASCADE)

