from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', include('meal_app.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('api/', include('blog_api.urls', namespace='blog_api')),

]