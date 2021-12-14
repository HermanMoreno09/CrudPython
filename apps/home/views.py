# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect

from apps.home.forms import ClientForm
from apps.home.models import Cliente


@login_required(login_url="/login/")
def index(request):
    data_cliente = Cliente.objects.all()

    if request.method == "POST":
        form = ClientForm(request.POST)

        if form.is_valid():
            info_form = form.cleaned_data

            addCliente = Cliente(nombre=info_form['nombre'],apellido=info_form['apellido'],email=info_form['email'],telefono=info_form['telefono'])
            addCliente.save()
    else:
        form = ClientForm()        

    return render(request, "home/index.html", {"form": form, "data_cliente":data_cliente})

@login_required(login_url="/login/")
def delete_client(request,id_client):
    data_host = Cliente.objects.get(id=id_client)
    data_host.delete()

    return HttpResponseRedirect('/')

@login_required(login_url="/login/")
def data_cliente(request, id_client):
    data_cliente = Cliente.objects.filter(id=id_client)

    if request.method == "POST":
        Cliente.objects.filter(id=id_client).update(nombre=request.POST['nombre'],apellido=request.POST['apellido'],email=request.POST['email'],telefono=request.POST['telefono'])
        return HttpResponseRedirect('/')    

    return render(request, "home/data_cliente.html", {"data_cliente":data_cliente})