from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from rimov.usuario import views as v


app_name = 'usuario'


urlpatterns = [
    path('', v.FuncionarioListView.as_view(), name='funcionario_list'),
    path('login/', LoginView.as_view(), name='login'),
    path(
        'logout/',
        LogoutView.as_view(),
        # {'next_page': settings.LOGOUT_REDIRECT_URL},
        name='logout'
    ),
    path('add/', v.FuncionarioCreateView.as_view(), name='funcionario_create'),
    path('<int:pk>/update/', v.FuncionarioUpdateView.as_view(), name='funcionario_update'),
    path('<int:pk>/delete/', v.FuncionarioDeleteView.as_view(), name='funcionario_delete'),
]
