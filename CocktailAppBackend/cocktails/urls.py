from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.UserList.as_view()),

    path('ingredients/', views.IngredientList.as_view()),

    path('cocktails/', views.CocktailList.as_view()),
    path('cocktails/<int:pk>/', views.CocktailDetails.as_view()),

    path('reviews/', views.ReviewList.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetails.as_view())
]
