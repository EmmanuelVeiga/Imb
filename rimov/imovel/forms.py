from .models import Imovel
from django import forms


class ImovelForm(forms.ModelForm):

    class Meta:
        model = Imovel
        fields = '__all__'
        imagens = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
