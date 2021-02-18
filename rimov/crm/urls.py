from django.urls import include, path
from rimov.crm import views as v


app_name = 'crm'


pf_urlpatterns = [
    path('', v.pf_list, name='pf_list'),
    path('add/', v.PFCreate.as_view(), name='pf_create'),
    # path('<int:pk>/', v.pf_detail, name='pf_detail'),
    path('<int:pk>/update/', v.PFUpdate.as_view(), name='pf_update'),
    # path('<int:pk>/delete/', v.pf_delete, name='pf_delete'),
]

pj_urlpatterns = [
    path('', v.pj_list, name='pj_list'),
    path('add/', v.PJCreate.as_view(), name='pj_create'),
    # path('<int:pk>/', v.pj_detail, name='pj_detail'),
    path('<int:pk>/update/', v.PJUpdate.as_view(), name='pj_update'),
    # path('<int:pk>/delete/', v.pj_delete, name='pj_delete'),
]


urlpatterns = [
    path('pessoa-fisica/', include(pf_urlpatterns)),
    path('pessoa-juridica/', include(pj_urlpatterns)),
]
