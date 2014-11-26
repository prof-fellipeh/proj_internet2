from django.conf.urls import patterns, include, url

from django.contrib import admin
from cadastro.views import *

admin.autodiscover()

urlpatterns = patterns('',

url(r'^cidade/$', 'cadastro.views.lista_cidades', name='lista_cidade'),
url(r'^cidade/novo/$', 'cadastro.views.edita_cidade', name='nova_cidade'),
url(r'^cidade/(?P<cidade_id>\d+)/$', 'cadastro.views.edita_cidade', name='edita_cidade'),
url(r'^cidade/excluir/(?P<cidade_id>\d+)/$', 'cadastro.views.excluir_cidade', name='del_cidade'),


    url(r'^admin/', include(admin.site.urls)),
)
