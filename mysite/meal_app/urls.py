from django.urls import path
from . import views

urlpatterns = [
    path('meals/', views.get_meals, name = "get_meals"),
    path('meals/<int:id>/',views.meal_detail, name = "meal_detail"),
    path('ip/', views.get_ip, name = "get_ip"),
    path('github/', views.get_github, name = "get_git"),
    path('github/client/', views.github_client, name='github_client'),
    path('oxford/', views.get_oxford, name = "get_oxford"),
]