from django.contrib import admin
from .models import Cocktail, Collection


# Register your models here.
admin.site.register(Collection)
admin.site.register(Cocktail)