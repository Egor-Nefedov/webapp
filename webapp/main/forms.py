from .models import Articles
from django.forms import ModelForm,TextInput

class  ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name', 'number', 'email', 'app']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'ФИО'
            }),
            'number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'app': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сообщение'
            })
        }