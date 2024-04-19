from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    product_name = models.CharField(
        max_length=150, verbose_name="наименование", help_text="Введите название товара"
    )
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f"{self.product_name} {self.description}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    product_name = models.CharField(
        max_length=250,
        verbose_name="наименование",
        help_text="Введите название товара",
    )
    description = models.TextField(
        **NULLABLE,
        verbose_name="Описание",
    )
    images = models.ImageField(
        upload_to="images",
        verbose_name="Изображение",
        **NULLABLE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(
        verbose_name="Дата создания(записи в БД",
        **NULLABLE,
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата последнего изменения(записи в БД",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.product_name} {self.description} {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["product_name"]
