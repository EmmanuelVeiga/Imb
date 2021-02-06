from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rimov.usuario.models import Usuario
from rimov.utils.decorators import LoginRequiredMixin, StaffRequiredMixin
from .forms import UsuarioForm


class UsuarioListView(ListView):
    model = Usuario


class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'usuario/usuario_form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy("usuario:usuario_list")   
        


class UsuarioUpdateView(UpdateView):
    model = Usuario
    fields = '__all__'
    success_url = 'usuario:usuario_list'

    def get_success_url(self):
        messages.success(self.request, 'Dados do usuário atualizados com sucesso na plataforma!')
        return reverse(self.success_url)


class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = 'usuario:usuario_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à esse usuário, permissão negada!')
        return redirect(self.success_url)
