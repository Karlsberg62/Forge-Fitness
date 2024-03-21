from . import views
from django.urls import include, path

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/", include("allauth.urls")),
    path("profile/", views.profile, name="profile"),
    path("classes/", views.SessionList.as_view(), name="classes"),
    path("<slug:slug>/",views.SessionDetail.as_view(), name="session-detail"),
    path("<slug:slug>/add_comment/", views.add_comment, name="add-comment"),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit-comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete-comment'),
    path('profile/edit_settings/',views.UserEditView.as_view(), name="edit_settings"),
    path('profile/edit_profile/', views.EditProfileView.as_view(), name="edit_profile"),
    path('profile/delete_account/', views.delete_account, name='delete_account'),
]