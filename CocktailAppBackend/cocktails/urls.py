from django.urls import path
from . import views

urlpatterns = [
    path('customers', views.UserList.as_view()),

    path('reviews', views.ReviewList.as_view()),
    path('reviews/<int:pk>/', views.ReviewList.as_view())
]
