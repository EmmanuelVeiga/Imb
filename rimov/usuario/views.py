from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Funcionario
from .forms import UserAdminCreationForm


class FuncionarioListView(ListView):
    model = Funcionario


def funcionario_create(request):
    form = UserAdminCreationForm(request.POST or None)
    template_name = 'usuario/funcionario_form.html'

    if form.is_valid():
        # Pega email para filtrar User.
        email = form.cleaned_data['email']
        user = User.objects.filter(email=email).first()
        if user:
            msg = 'Email já cadastro. Favor fazer login.'
            messages.error(request, msg)
            return redirect(reverse_lazy('usuario:login'))
        else:
            user = form.save()
            # Cria Funcionario
            funcionario, _ = Funcionario.objects.get_or_create(
                usuario=user,
                cri=form.cleaned_data['cri']
            )
        return redirect(reverse_lazy('usuario:funcionario_list'))
    return render(request, template_name, {'form': form})


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = '__all__'
    success_url = 'usuario:funcionario_list'

    def get_success_url(self):
        msg = 'Dados do usuário atualizados com sucesso.'
        messages.success(self.request, msg)
        return reverse(self.success_url)


class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    success_url = 'usuario:funcionario_list'

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
            messages.error(request, 'Há dependências ligadas a esse usuário, permissão negada.')
        return redirect(self.success_url)
