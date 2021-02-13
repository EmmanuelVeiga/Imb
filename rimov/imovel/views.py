from .forms import ImovelForm
from .models import Imovel, Galeria
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView


def imovel_list(request):
    imoveis = Imovel.objects.all()
    return render(request, 'imovel/imovel_list.html', {"imoveis": imoveis})


def imovel_create(request):
    form = ImovelForm(request.POST or None, request.FILES)
    if request.method == "POST":
        files = request.FILES.getlist('imagens')
        if form.is_valid():
            imovel = form.save()  # Pega a instância do Imovel.
            for file in files:
                Galeria.objects.create(imovel=imovel, imagem=file)
            return redirect('imovel:imovel_list')
    return render(request, 'imovel/imovel_form.html', {'form': form})


def imovel_detail(request, id):
    imovel = get_object_or_404(Imovel, pk=id)
    return render(request, 'imovel/imovel_detail.html', {'imovel': imovel})


def imovel_update(request, id):
    imovel = get_object_or_404(Imovel, pk=id)
    form = ImovelForm(instance=imovel)
    if(request.method == 'POST'):
        form = ImovelForm(request.POST, request.FILES, instance=imovel)

        if(form.is_valid()):
            imovel = form.save(commit=False)
            imovel.save()
            return redirect('imovel:imovel_list')
        else:
            return render(request, 'imovel/imovel_update.html', {'form': form, 'imovel': imovel})
    elif(request.method == 'GET'):
        return render(request, 'imovel/imovel_update.html', {'form': form, 'imovel': imovel})


def imovel_delete(request, id):
    form = ImovelForm(request.POST)
    imovel = Imovel.objects.get(id=id)
    imovel.delete()
    return redirect('imovel:imovel_list')
    return render(request, 'imovel/imovel_delete.html', {'form': form})


def login_page(request):
    context = {
        'error_msg': ''
    }

    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(settings.LOGIN_URL_REDIRECT)
        else:
            context = {
                'error_msg': 'Senha e/ou usuário inválido.'
            }
            return render(request, 'registration/login.html', context)

    return render(request, 'registration/login.html', context)
