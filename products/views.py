from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


def home_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/index.html', context)


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, f"Your account has been created successfully")
        return redirect('login')
    return render(request, 'products/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'products/login.html', {'error_message': 'Incorrect username or password.'})
    else:
        return render(request, 'products/login.html')


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
