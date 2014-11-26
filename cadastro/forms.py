# -*- coding: utf-8 -*-

from django.forms import ModelForm
from models import *


class CidadeForm(ModelForm):
    class Meta:
        model = Cidade