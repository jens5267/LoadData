from django import forms

from .models import Load

class LoadForm(forms.ModelForm):
    class Meta:
        model = Load
        fields = [
            'first_input',
            'second_input'
        ] 