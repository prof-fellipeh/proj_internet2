# -*- coding: utf-8 -*-

from django.db import models


Status_Lista = (
    ('A', 'Ativo'),
    ('I', 'Inativo')
)

class Contato(models.Model):
    status = models.CharField(verbose_name=u'Status', max_length=1, default='A', choices=Status_Lista)
    nome = models.CharField(verbose_name=u'Nome', max_length=50)
    doc = models.CharField(verbose_name=u'CPF/CNPJ', max_length=20, unique=True)
    telefone = models.CharField(verbose_name=u'Telefone', max_length=25, null=True, blank=True)
    data_nascimento = models.DateField(verbose_name=u'Dt. Nasc.', null=True, blank=True)
    email = models.EmailField(verbose_name=u'E-Mail', max_length=100)
    salario = models.DecimalField(verbose_name=u'Salário', decimal_places=2, max_digits=18, default=0)

    def __unicode__(self):
        return self.nome