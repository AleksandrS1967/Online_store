# Generated by Django 4.2 on 2024-05-28 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0009_alter_product_product_activ"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_activ",
            field=models.BooleanField(default=False, verbose_name="признак публикации"),
        ),
    ]
