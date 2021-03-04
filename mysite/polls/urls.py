from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api_test/<int:id>', views.api_details, name='api_get_details'),
    path('api_test/', views.api_index, name='api_get'),
    path('403/', views.response_error_handler),
    path('<slug:pk>/amp', views.MusicianDetailView.as_view(), name='musician-detail'),
    path('persons/', views.PersonListView.as_view(), name='person-list'),
    path('persons/create', views.PersonCreate.as_view(), name='person-create'),
    path('persons/<slug:pk>/update', views.PersonUpdate.as_view(), name='person-update'),
    path('persons/<slug:pk>/delete', views.PersonDelete.as_view(), name='person-delete'),
    path('<slug:pk>/person', views.MusicianDetailView.as_view(), name='person-detail'),
    path("middleware/", views.index),

]