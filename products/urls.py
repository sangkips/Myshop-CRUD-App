from django.urls import path

from .views import home_view, \
    create_product, \
    update_product, \
    delete_product

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_product, name='create-product'),
    path('update/', update_product, name='update-product'),
    path('delete/>', delete_product, name='delete-url'),
]
