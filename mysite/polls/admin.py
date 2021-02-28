from django.contrib import admin
from .models import Musician,Person,Album,Turner,Membership,Group

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Musician)
admin.site.register(Person)
admin.site.register(Album)
admin.site.register(Turner)
admin.site.register(Membership)
admin.site.register(Group)