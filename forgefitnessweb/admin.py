from django.contrib import admin
from .models import Classes, Profile, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Classes)