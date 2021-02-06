from django.urls import path
from rimov.usuario import views as v


app_name = 'usuario'


urlpatterns = [
    path('', v.FuncionarioListView.as_view(), name='funcionario_list'),
    path('add/', v.FuncionarioCreateView.as_view(), name='funcionario_create'),
    path('<int:pk>/update/', v.FuncionarioUpdateView.as_view(), name='funcionario_update'),
    path('<int:pk>/delete/', v.FuncionarioDeleteView.as_view(), name='funcionario_delete'),
]
