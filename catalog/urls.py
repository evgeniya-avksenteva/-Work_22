from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ContactView, ProductListByCategoryView
from django.views.decorators.cache import cache_page


app_name = CatalogConfig.name


urlpatterns = [
    path("", ProductListView.as_view(), name='product_list'),
    path("products/category/<int:category_id>/", ProductListByCategoryView.as_view(), name="category_products"),
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path("product/create", ProductCreateView.as_view(), name='product_create'),
    path("product/<int:pk>/update", ProductUpdateView.as_view(), name='product_update'),
    path("product/<int:pk>/delete", ProductDeleteView.as_view(), name='product_delete'),
    path("contact/", ContactView.as_view(), name="contact"),
]
