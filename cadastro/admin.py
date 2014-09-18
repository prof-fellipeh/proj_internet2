# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

class ContatoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contato, ContatoAdmin)