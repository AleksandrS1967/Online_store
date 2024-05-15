from django.contrib import admin

from catalog.models import Category, Product, Version
from publication.models import Publication


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description')


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'publication_activ')
    list_filter = ('name',)
    search_fields = ('name', 'slug',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'version_number', 'version_name',)
    list_filter = ('product_name',)

