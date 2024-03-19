from .models import CommentReview, Profile
from django.contrib.auth.forms import UserChangeForm, User
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentReview
        fields = ('body','rating',)

class EditProfileForm(UserChangeForm):
    #Normal User
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'})) 
    last_name= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'})) 
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    #Admin
    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-control'}))
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-control'}))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-control'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'})) 
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'})) 

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_superuser','is_staff','is_active','date_joined','last_login')
