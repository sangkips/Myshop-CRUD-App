from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ProductForm, CreateUserForm
from .models import Product


def home_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/index.html', context)


def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'products/register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'products/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        return render(request, 'products/login.html')


def user_page(request):
    context = {}
    return render(request, 'products/user.html', context)


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
