from django.contrib import admin
from .models import Sessions, Profile, CommentReview
from django import forms

# Register your models here.
admin.site.register(Profile)
admin.site.register(CommentReview)
admin.site.register(Sessions)
