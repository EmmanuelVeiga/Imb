from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from rimov.usuario import views as v
from rimov.usuario.forms import LoginForm


app_name = 'usuario'


urlpatterns = [
    path('', v.FuncionarioListView.as_view(), name='funcionario_list'),
    path('login/', LoginView.as_view(form_class=LoginForm), name='login'),
    path(
        'logout/',
        LogoutView.as_view(),
        # {'next_page': settings.LOGOUT_REDIRECT_URL},
        name='logout'
    ),
    path('add/', v.funcionario_create, name='funcionario_create'),
    path('<int:id>/', v.funcionario_detail, name='funcionario_detail'),
    path('<int:pk>/update/', v.FuncionarioUpdateView.as_view(), name='funcionario_update'),
    path('<int:pk>/delete/', v.FuncionarioDeleteView.as_view(), name='funcionario_delete'),
]
