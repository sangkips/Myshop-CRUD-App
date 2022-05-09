from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Product


def home_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/index.html', context)


def create_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'products/create.html', context)


def update_product(request, pk):
    products = Product.objects.get(id=pk)
    form = ProductForm(instance=products)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
        'products': products
    }
    return render(request, 'products/update.html', context)


def delete_product(request, pk):
    products = Product.objects.get(id=pk)

    if request.method == 'POST':
        products.delete()
        return redirect('home')
    context = {
        'product': products,
    }
    return render(request, 'products/delete.html', context)
