# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from apps.home.models import Cliente


class tableCliente(admin.ModelAdmin):
    list_display = ("nombre","apellido","email","telefono",)
    search_fields = ("nombre","apellido",)


admin.site.register(Cliente, tableCliente)
