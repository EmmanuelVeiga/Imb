from django.urls import path
from rimov.imovel import views as v


app_name = 'imovel'


urlpatterns = [
    path('', v.imovel_list, name='imovel_list'),
    path('add/', v.imovel_create, name='imovel_create'),
    path('<int:id>/', v.imovel_detail, name='imovel_detail'),
    path('<int:id>/update/', v.imovel_update, name='imovel_update'),
    path('<int:id>/delete/', v.imovel_delete, name='imovel_delete'),
]
