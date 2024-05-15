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
        verbose_name = "категория"   # Настройка для наименования одного объекта
        verbose_name_plural = "категории"   # Настройка для наименования набора объектов


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


class Version(models.Model):
    product_name = models.ForeignKey(Product, verbose_name='наименование', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name="наименование", help_text="Введите название товара")
    version_number = models.PositiveIntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=50, verbose_name='название версии')
    current_version = models.BooleanField(verbose_name='признак текущей версии', default=True)

    def __str__(self):
        return f'{self.product_name} номер {self.version_number} название {self.version_name}'

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"




