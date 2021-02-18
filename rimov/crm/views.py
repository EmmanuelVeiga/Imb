from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import PessoaFisicaForm, PessoaJuridicaForm
from .models import PessoaFisica, PessoaJuridica


def pf_list(request):
    template_name = 'crm/pessoa_fisica_list.html'
    object_list = PessoaFisica.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


class PFCreate(CreateView):
    model = PessoaFisica
    form_class = PessoaFisicaForm
    success_url = reverse_lazy('crm:pf_list')


def pj_list(request):
    template_name = 'crm/pessoa_juridica_list.html'
    object_list = PessoaJuridica.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


class PJCreate(CreateView):
    model = PessoaJuridica
    form_class = PessoaJuridicaForm
    success_url = reverse_lazy('crm:pj_list')
