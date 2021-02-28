from django.contrib import admin
from .models import Meal

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Meal)
