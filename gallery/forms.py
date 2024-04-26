# gallery/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Artwork
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'artist', 'description', 'image', 'price']