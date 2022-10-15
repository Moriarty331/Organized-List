from django import forms
from .models import *
from django.forms import ModelForm, TextInput, EmailInput


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('lists',)
        widgets = {
            'lists': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 200px;' 'height: 40px;' 'border: none;' 'margin-top: 2px;' 'margin-right: 0;',
                'placeholder': 'Title'
                })
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('todos',)
        widgets = {
            'todos': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 310px;' 'height: 40px;' 'border: none;' 'margin-top: 2px;' 'margin-right: 0;',
                'placeholder': 'Add a new list'
                })
        }
        