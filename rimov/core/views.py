from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def team(request):
    template_name = 'team.html'
    return render(request, template_name)


def pgrid(request):
    template_name = 'property-grid.html'
    return render(request, template_name)


def contact(request):
    template_name = 'contact.html'
    return render(request, template_name)


