from django.contrib.auth.models import User

from .models import Product
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class ProductForm(ModelForm):
    class Meta:

        model = Product

        fields = ('title', 'price', 'description', 'featured_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'Featured_image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price (Kshs)'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product description'}),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User

        fields = ('username', 'email', 'password1', 'password2')
'''
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }
'''