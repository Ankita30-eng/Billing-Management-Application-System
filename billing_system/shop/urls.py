from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('add-product/', views.add_product, name='add_product'),

    path('products/', views.product_list, name='product_list'),

    path('create-bill/', views.create_bill, name='create_bill'),

    path('bills/', views.bill_list, name='bill_list'),

    path('invoice/<int:id>/', views.invoice, name='invoice'),

]