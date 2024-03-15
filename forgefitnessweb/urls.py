from . import views
from django.urls import include, path

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/", include("allauth.urls")),
    path("profile/", views.profile, name="profile")
]