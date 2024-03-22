from .models import CommentReview, Profile, AnonContact
from django.contrib.auth.forms import UserChangeForm, User
from django.contrib.auth import password_validation
from allauth.account.forms import SignupForm
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentReview
        fields = ('body','rating',)

class EditSettingsForm(UserChangeForm):
    #Normal User
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'})) 
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'})) 
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    #Admin
    #is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-control'}), required=False),
    #is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-control'}), required=False)
    #is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-control'}), required=False, initial='True')
    #date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'})) 
    #last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'})) 

    #Django documentation integrating validation with Validate_Password. Returns None if valid, otherwise return ValidationError.
    def clean_password(self):
            password = self.cleaned_data.get("password")
            if password:
                try:
                    password_validation.validate_password(password, self.instance)
                except forms.ValidationError as error:
                    self.add_error('password', error)
            return password

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username', 'password')

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

class AnonContactForm(forms.ModelForm):
    class Meta:
        model = AnonContact
        fields = ['name', 'email', 'message']