from django.contrib import admin
from .models import Actor, Comment, Character

# Register your models here.
admin.site.register(Actor)
admin.site.register(Comment)
admin.site.register(Character)