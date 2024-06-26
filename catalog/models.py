from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    product_name = models.CharField(
        max_length=150, verbose_name="наименование", help_text="Введите название товара"
    )
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f"{self.product_name} {self.description}"

    class Meta:
        verbose_name = "категория"  # Настройка для наименования одного объекта
        verbose_name_plural = "категории"  # Настройка для наименования набора объектов


class Product(models.Model):
    product_activ = models.BooleanField(
        verbose_name="признак публикации", default=False
    )
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
    owner = models.ForeignKey(
        User,
        verbose_name="владелец",
        help_text="Укажите владельца продукта",
        on_delete=models.CASCADE,
        **NULLABLE
    )

    def __str__(self):
        return f"{self.product_name}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["product_name"]
        permissions = [
            ('can_edit_description', 'Can edit description'),
            ('can_edit_category', 'Can edit Category'),
            ('can_edit_product_activ', 'Can edit Product_activ')
        ]


class Version(models.Model):
    product = models.ForeignKey(
        Product, verbose_name="продукт", on_delete=models.CASCADE
    )
    version_number = models.PositiveIntegerField(verbose_name="номер версии")
    version_name = models.CharField(max_length=50, verbose_name="название версии")
    current_version = models.BooleanField(
        verbose_name="признак текущей версии", default=True
    )

    def __str__(self):
        return (
            f"{self.product} номер {self.version_number} название {self.version_name}"
        )

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"
