from .models import CommentReview
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentReview
        fields = ('body','rating',)