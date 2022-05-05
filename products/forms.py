from .models import Product
from django import forms
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:

        model = Product

        fields = ('title', 'price', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price (Kshs)'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product description'}),
        }

