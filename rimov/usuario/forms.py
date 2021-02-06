from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='E-mail')

    class Meta:
        model = User


class UserAdminCreationForm(UserCreationForm):
    ''' Cadastro geral de Usuário. '''
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.CharField(label='E-mail')
    # cpf = forms.CharField(label='CPF')  # UserProfile

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def save(self, commit=True):
        instance = super(UserAdminCreationForm, self).save(commit=False)
        # Salva username = email
        instance.username = self.cleaned_data['email']
        if commit:
            instance.save()
        return instance
