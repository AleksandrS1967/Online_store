from django import forms
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


list_valid = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ("product_name", "category", "price", "images", "description")

    def clean_product_name(self):
        cleaned_data: str = self.cleaned_data.get("product_name")
        for word in list_valid:
            if word in cleaned_data.lower():
                raise forms.ValidationError("название продукта не прошло валидацию")

        return cleaned_data

    def clean_description(self):
        cleaned_data: str = self.cleaned_data.get("description")
        for word in list_valid:
            if word in cleaned_data.lower():
                raise forms.ValidationError("название продукта не прошло валидацию")

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
