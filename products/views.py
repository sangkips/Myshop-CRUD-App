from django.shortcuts import render, redirect

from .forms import ProductForm
from products.models import Product


def home_view(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, 'products/index.html', context)


def create_product(request):
    form = ProductForm

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'products/create.html', context)


def update_product(request):
    return render(request, 'products/update.html')


def delete_product(request):
    return render(request, 'products/index.html')
