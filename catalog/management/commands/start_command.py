import json
from django.core.management import BaseCommand
from catalog.models import Category, Product
from django.db import connection
import os


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(os.path.join('fixtures', 'category_data.json'), encoding='utf-8') as category:
            data = json.load(category)
            return data

    # Здесь мы получаем данные из фикстурв с категориями

    @staticmethod
    def json_read_products():
        with open(os.path.join('fixtures', 'product_data.json'), encoding='utf-8') as product:
            data = json.load(product)
            return data

    # Здесь мы получаем данные из фикстурв с продуктами

    def handle(self, *args, **options):

        with connection.cursor() as cur:
            cur.execute(f'TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;')

        # Удалите все продукты
        # Удалите все категории

        Category.objects.all().delete()
        Product.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(product_name=category["fields"]["product_name"], description=category["fields"]["description"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(product_name=product["fields"]["product_name"],
                        # получаем категорию из базы данных для корректной связки объектов
                        category=Category.objects.get(pk=product["fields"]["category"]),
                        price=product["fields"]["price"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
