from django.urls import include, path
from rimov.crm import views as v


app_name = 'crm'


pf_urlpatterns = [
    path('', v.pf_list, name='pf_list'),
    # path('add/', v.pf_create, name='pf_create'),
    # path('<int:id>/', v.pf_detail, name='pf_detail'),
    # path('<int:id>/update/', v.pf_update, name='pf_update'),
    # path('<int:id>/delete/', v.pf_delete, name='pf_delete'),
]

pj_urlpatterns = [
    path('', v.pj_list, name='pj_list'),
    # path('add/', v.pj_create, name='pj_create'),
    # path('<int:id>/', v.pj_detail, name='pj_detail'),
    # path('<int:id>/update/', v.pj_update, name='pj_update'),
    # path('<int:id>/delete/', v.pj_delete, name='pj_delete'),
]


urlpatterns = [
    path('pessoa-fisica/', include(pf_urlpatterns)),
    path('pessoa-juridica/', include(pj_urlpatterns)),
]
