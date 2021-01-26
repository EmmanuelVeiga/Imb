from django.urls import path
from rimov.usuario import views as v


app_name = 'usuario'


urlpatterns = [
    path('', v.UsuarioListView.as_view(), name='usuario_list'),
    path('add/', v.UsuarioCreateView.as_view(), name='usuario_create'),
    path('<int:pk>/update/', v.UsuarioUpdateView.as_view(), name='usuario_update'),
    path('<int:pk>/delete/', v.UsuarioDeleteView.as_view(), name='usuario_delete'),
]
