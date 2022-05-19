from .models import Product
from django import forms
from django.forms import ModelForm


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
