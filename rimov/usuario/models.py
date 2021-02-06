from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy


class Funcionario(models.Model):
    TIPOS_USUARIOS = (
        ('ADM', 'Administrador'),
        ('COR', 'Corretor'),
    )
    usuario = models.OneToOneField(User, verbose_name='usuário', on_delete=models.CASCADE)
    tipo = models.CharField(
        'tipo do usuário',
        max_length=15,
        choices=TIPOS_USUARIOS,
        default='CORRETOR',
        help_text='Campos obrigatórios'
    )
    avatar = models.ImageField(
        default='media/media/avatar.jpg',
        upload_to='media/',
        blank=True,
        null=True
    )
    cri = models.CharField('registro CRI', max_length=100, blank=True, null=True)
    telefone = models.CharField('telefone', max_length=100, blank=True, null=True)
    instagram = models.CharField('perfil Instagram', max_length=400, blank=True, null=True)
    facebook = models.CharField('perfil Facebook', max_length=400, blank=True, null=True)

    class Meta:
        ordering = ('usuario__first_name',)
        verbose_name = 'funcionário'
        verbose_name_plural = 'funcionários'

    def __str__(self):
        if self.usuario.get_full_name():
            return self.usuario.get_full_name()
        return self.usuario.email

    def get_absolute_url(self):
        return reverse_lazy('usuario:funcionario_update', args=[str(self.pk)])

    def get_delete_url(self):
        return reverse_lazy('usuario:funcionario_delete', args=[str(self.pk)])
