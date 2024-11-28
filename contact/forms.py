from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'class-a class-b',
                'placeholder': 'Escreva seu nome'
            }
        ),
        label='Primeiro nome',
        help_text='Texto de ajuda',
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
        
    def clean(self):
        #validação para mais de um campo
        cleaned_data = self.cleaned_data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if first_name == last_name:
            msg = ValidationError(
                    'primeiro e último nome não podem ser iguais',
                    code='inválido'
                )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        return super().clean()
    def clean_first_name(self):
        #validação para um único campo
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Mensagem do erro',
                    code='inválido'
                )
            )
        return first_name