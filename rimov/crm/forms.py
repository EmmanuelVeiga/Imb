from django import forms
from .models import PessoaFisica, PessoaJuridica


class PessoaFisicaForm(forms.ModelForm):

    class Meta:
        model = PessoaFisica
        fields = (
            'nome',
            'sobrenome',
            'cpf',
            'rg',
            'endereco',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'cep',
        )


class PessoaJuridicaForm(forms.ModelForm):

    class Meta:
        model = PessoaJuridica
        fields = (
            'razao_social',
            'nome_fantasia',
            'cnpj',
            'inscricao_estadual',
            'inscricao_municipal',
            'endereco',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'cep',
        )
