from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api_test/<int:id>', views.api_details, name='api_get_details'),
    path('api_test/', views.api_index, name='api_get'),
    #path('api_test_post/', views.api_post, name='api_post'),
]