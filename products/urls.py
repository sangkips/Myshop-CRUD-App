from django.urls import path

from .views import home_view, \
    create_product, \
    update_product, \
    delete_product, \
    login_view, \
    register_view

urlpatterns = [
    path('home/', home_view, name='home'),

    path('', login_view, name='login'),
    path('register/', register_view, name='register-user'),

    path('create/', create_product, name='create-product'),
    path('update//<str:pk>', update_product, name='update-product'),
    path('delete//<str:pk>', delete_product, name='delete-product'),


]
