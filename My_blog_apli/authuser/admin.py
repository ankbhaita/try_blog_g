from django.contrib import admin
from .models import User

@admin.register(User)
class PostModelAdmin(admin.ModelAdmin):
	list_display=['email','name']

# Register your models here.
