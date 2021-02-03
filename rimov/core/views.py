from django.shortcuts import render
from rimov.imovel.models import Imovel
from rimov.usuario.models import Usuario


def index(request):
    template_name = 'index.html'
    imoveis = Imovel.objects.all()
    context = {'imoveis': imoveis}
    return render(request, template_name, context)


def painel(request):
    template_name = 'painel.html'
    return render(request, template_name)


def team(request):
    template_name = 'team.html'
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request, template_name, context)


def pgrid(request):
    template_name = 'property-grid.html'
    imoveis = Imovel.objects.all()
    context = {'imoveis': imoveis}
    return render(request, template_name, context)


def contact(request):
    template_name = 'contact.html'
    return render(request, template_name)


