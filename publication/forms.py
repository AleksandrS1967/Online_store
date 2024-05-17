from django import forms

from catalog.forms import list_valid, StyleFormMixin
from publication.models import Publication


class PublicationForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('name', 'description', 'image', 'publication_activ', 'counter')

        def clean_name(self):
            cleaned_data: str = self.cleaned_data['name']

            for word in list_valid:
                if word.lower() in cleaned_data.lower():
                    raise forms.ValidationError('Название не прошло валидацию')

            return cleaned_data

        def clean_description(self):
            cleaned_data: str = self.cleaned_data['description']

            for word in list_valid:
                if word.lower() in cleaned_data.lower():
                    raise forms.ValidationError('Описание не прошло валидацию')

            return cleaned_data
