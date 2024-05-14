from django import forms

from catalog.models import Product

list_valid = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'category', 'price', 'images', 'description')

    def clean_product_name(self):
        cleaned_data: str = self.cleaned_data.get('product_name')
        for word in list_valid:
            if word in cleaned_data.lower():
                raise forms.ValidationError('название продукта не прошло валидацию')

        return cleaned_data

    def clean_description(self):
        cleaned_data: str = self.cleaned_data.get('description')
        for word in list_valid:
            if word in cleaned_data.lower():
                raise forms.ValidationError('название продукта не прошло валидацию')

        return cleaned_data
