from django.core.cache import cache
from config.settings import CACHE_ENABLED
from catalog.models import Category


def get_categories_from_cache():
    if not CACHE_ENABLED:
        return Category.objects.all()
    categories = cache.get('categories')

    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set('categories', categories)
    return categories

