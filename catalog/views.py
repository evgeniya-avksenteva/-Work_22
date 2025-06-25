from gc import get_objects
from itertools import product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import Product
from django.shortcuts import render, get_object_or_404


class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image", "category", "purchase_price")
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "image", "category", "purchase_price")
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
