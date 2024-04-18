from django.db import models


# Create your models here.


class Product(models.Model):
    pass

    # product_name = models.CharField(max_length=250, verbose_name='наименование')
    # description = last_name = models.CharField(max_length=350, verbose_name='описание')
    # images =

    def __str__(self):
        pass
        # return f'{self.product_name} {self.description} {self.price}'

    class Meta:
        pass


class Category(models.Model):
    pass

    def __str__(self):
        pass

    class Meta:
        pass
