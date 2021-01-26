from django.urls import path
from rimov.core import views as v


app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
    path('team', v.team, name='team'),
    path('pgrid', v.pgrid, name='pgrid'),
    path('contact', v.contact, name='contact'),
]
