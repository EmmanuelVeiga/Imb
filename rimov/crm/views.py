from django.shortcuts import render
from .models import PessoaFisica, PessoaJuridica


def pf_list(request):
    template_name = 'crm/pessoa_fisica_list.html'
    object_list = PessoaFisica.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def pj_list(request):
    template_name = 'crm/pessoa_juridica_list.html'
    object_list = PessoaJuridica.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)
