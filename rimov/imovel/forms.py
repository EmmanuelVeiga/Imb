from django.forms import ModelForm
from django.forms import ClearableFileInput
from .models import Imovel
from django import forms


class ImovelForm(forms.ModelForm):

    class Meta:
        model = Imovel
        fields = '__all__'
        imagens = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
