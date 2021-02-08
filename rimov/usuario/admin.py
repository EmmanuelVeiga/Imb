from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Funcionario


class FuncionarioInline(admin.StackedInline):
    model = Funcionario
    can_delete = False
    fk_name = 'usuario'


class CustomUserAdmin(UserAdmin):
    inlines = (FuncionarioInline, )
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'get_tipo')
    search_fields = ('first_name', 'last_name', 'email', 'cri')

    def save_model(self, request, obj, form, change):
        obj.username = obj.email
        obj.save()
        super().save_model(request, obj, form, change)

    def get_tipo(self, instance):
        return instance.funcionario.get_tipo_display()
    get_tipo.short_description = 'Tipo'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
