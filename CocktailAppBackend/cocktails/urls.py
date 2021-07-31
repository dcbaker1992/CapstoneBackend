from django.urls import path
from . import views

urlpatterns = [

    path('cocktails/', views.CocktailList.as_view()),
    path('collection/', views.CollectionList.as_view()),
    path('collection/cocktails/<int:collection_id>', views.CocktailsInCollection.as_view()),
    path('cocktails/<int:pk>/', views.CocktailDetails.as_view()),
    path('collection/<int:pk>/', views.CollectionDetails.as_view()),

]
