from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImovelForm
from .models import Imovel, Galeria


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
    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES, instance=imovel)

        if form.is_valid():
            imovel = form.save(commit=False)
            imovel.save()
            return redirect('imovel:imovel_list')

    context = {'form': form, 'imovel': imovel}
    return render(request, 'imovel/imovel_form.html', context)


def imovel_delete(request, id):
    imovel = Imovel.objects.get(id=id)
    imovel.delete()
    return redirect('imovel:imovel_list')


def imagem_update(request, id):
    galeria = Galeria.objects.get(id=id)
    if request.method == 'POST':
        imagem = request.FILES.get('imagem')
        galeria.imagem = imagem
        galeria.save()
    return redirect(galeria.imovel)
