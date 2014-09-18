# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

class ContaReceberAdmin(admin.ModelAdmin):
    pass

admin.site.register(ContaReceber, ContaReceberAdmin)