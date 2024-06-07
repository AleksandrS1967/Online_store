from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ContactsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    VersionCreateView, CategoryListView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("product_delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),
    path("create/", ProductCreateView.as_view(), name="create_product"),
    path("create_version/", VersionCreateView.as_view(), name="create_version"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="update_product"),
    path("category_list/", CategoryListView.as_view(), name="list_category"),
]
