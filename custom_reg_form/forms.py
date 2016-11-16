from django.core.exceptions import ValidationError

from .models import ExtraInfo
from django.forms import ModelForm, forms


class ExtraInfoForm(ModelForm):
    def clean(self):
        cell_number = self.cleaned_data.get('cell_number', None)
        number = str(cell_number)
        if not len(number) == 10 or not number.isdigit():
            raise forms.ValidationError("Please enter a valid phone number")
        else:
            return self.cleaned_data

    class Meta:
        model = ExtraInfo
        fields = ('user', 'cell_number', 'id_passport_number', 'center')
