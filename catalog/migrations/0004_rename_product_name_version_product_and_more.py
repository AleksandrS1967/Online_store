# Generated by Django 5.0.6 on 2024-05-16 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_version_name_alter_version_product_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="version",
            old_name="product_name",
            new_name="product",
        ),
        migrations.RemoveField(
            model_name="version",
            name="name",
        ),
    ]
