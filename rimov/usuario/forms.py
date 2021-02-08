from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .constants import TIPOS_USUARIOS


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='E-mail')

    class Meta:
        model = User


class UserAdminCreationForm(UserCreationForm):
    ''' Cadastro geral de Usuário. '''
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.EmailField(label='E-mail')
    tipo = forms.ChoiceField(
        label='Tipo de funcionário',
        choices=TIPOS_USUARIOS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    avatar = forms.FileField(required=False)
    cri = forms.CharField(label='CRI', required=False)
    telefone = forms.CharField(label='Telefone', required=False)
    instagram = forms.CharField(label='Instagram', required=False)
    facebook = forms.CharField(label='Facebook', required=False)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'tipo',
            'avatar',
            'cri',
            'telefone',
            'instagram',
            'facebook',
        )

    def save(self, commit=True):
        instance = super(UserAdminCreationForm, self).save(commit=False)
        # Salva username = email
        instance.username = self.cleaned_data['email']
        if commit:
            instance.save()
        return instance
