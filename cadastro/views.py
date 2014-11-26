# -*- coding: utf-8 -*-

# Desenvolvido por: Fellipe

from django.shortcuts import render, render_to_response, redirect
from models import *
from forms import *
from django.template import RequestContext

def lista_cidades(request):
    cidades = Cidade.objects.all()

    return render(request, 'lista_cidade.html', locals())


def excluir_cidade(request, cidade_id=None):
    if cidade_id:
        Cidade.objects.get(pk=cidade_id).delete()

def edita_cidade(request, cidade_id=None):
    if cidade_id:
        v_cidade = Cidade.objects.get(pk=cidade_id)
    else:
        v_cidade = None

    if request.method == 'POST':
        form = CidadeForm(request.POST, instance=v_cidade)

        if form.is_valid():
            resultado = form.save()
            if resultado:
                return redirect('/cidade')
    else:
        form = CidadeForm(instance=v_cidade)

    return render(request, 'edita_cidade.html', locals())