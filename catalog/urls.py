from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, product_detail
app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name='home'),
    path("contacts/", contacts, name='contact'),
    path("product_detail/<int:pk>", product_detail, name="product_detail")

]
