# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('', views.index, name='home'),
    path("delete_cliente/<int:id_client>/",views.delete_client,name="home"),
    path("data_clioente/<int:id_client>/",views.data_cliente,name="home"),
]
