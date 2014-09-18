# -*- coding: utf-8 -*-

from django.db import models
from cadastro.models import Contato


class ContaReceber(models.Model):
    pago = models.BooleanField(verbose_name=u'Pago?', default=False)
    data_mov = models.DateField(verbose_name=u'Data Movimento')
    data_vencimento = models.DateField(verbose_name=u'Data Vencimento')
    valor = models.DecimalField(verbose_name=u'Valor', max_digits=18, decimal_places=2, default=0)
    descricao = models.CharField(verbose_name=u'Descrição', max_length=50)
    data_pagamento = models.DateField(verbose_name=u'Data Pagamento', null=True, blank=True)
    contato = models.ForeignKey(Contato, blank=True, null=True)


