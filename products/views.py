from django.shortcuts import render

from products.models import Product


def home_view(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, 'products/index.html', context)


def create_product(request):
    return render(request, 'products/create.html')


def update_product(request):
    return render(request, 'products/update.html')


def delete_product(request):
    return render(request, 'products/index.html')
