from gc import get_objects
from itertools import product


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy

from catalog.models import Product, Category
from django.shortcuts import render, get_object_or_404
from catalog.forms import ProductForm, ProductModeratorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from catalog.services import get_products_from_cache, get_products_by_category


class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Установите владельца товара
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if request.user != product.owner and not request.user.has_perm("catalog.can_delete_product"):
            raise PermissionDenied("У вас нет прав на удаление этого продукта.")
        return super().dispatch(request, *args, **kwargs)


class ProductListByCategoryView(ListView):
    model = Product
    template_name = "catalog/category_products.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, id=self.kwargs.get("category_id"))
        context["category"] = category
        return context


class ContactView(TemplateView):
    template_name = "catalog/contact.html"
