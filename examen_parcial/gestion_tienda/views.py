from collections import UserDict
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import datosUsuario
from .models import datosProducto

#Create your views here
def index(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        contraUsuario = request.POST.get('contraUsuario')
        usuarioInfo = authenticate(request, username=nombreUsuario, password=contraUsuario)
        if usuarioInfo is not None:
            login(request,usuarioInfo)
            return HttpResponseRedirect (reverse('gestion_tienda:panelNavegacion'))
        else:
            return HttpResponseRedirect (reverse('gestion_tienda:index'))
    return render(request,'ingresoUsuario.html')

@login_required(login_url='http://127.0.0.1:8000')
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('gestion_tienda:index'))

@login_required(login_url='http://127.0.0.1:8000')
def panelNavegacion(request):
    if request.user.datousuario.tipoUsuario == 'Administrador':
        if request.method == 'POST':
            nombreUsuario = request.POST.get('nombreUsuario')
            apellidoUsuario = request.POST.get('apellidoUsuario')
            emailUsuario = request.POST.get('emailUsuario')
            usernameUsuario = request.POST.get('usernameUsuario')
            contraUsuario = request.POST.get('contraUsuario')
            tipoUsuario = request.POST.get('tipoUsuario')
            nroCelular = request.POST.get('nroCelular')
            fechaIngreso = request.POST.get('fechaIngreso')

            usuarioNuevo = User.objects.create(
                username=usernameUsuario,
                email=emailUsuario,
            )

            usuarioNuevo.set_password(contraUsuario)
            usuarioNuevo.first_name = nombreUsuario
            usuarioNuevo.last_name = apellidoUsuario
            usuarioNuevo.is_staff = True
            usuarioNuevo.save()

            datosUsuario.objects.create(
                user=usuarioNuevo,
                tipoUsuario=tipoUsuario,
                nroCelular=nroCelular,
                fechaIngreso=fechaIngreso
            )
            return HttpResponseRedirect(reverse('gestion_tienda : panelNavegacion'))
        return render(request,'panelNavegacion.html',{
            'usuariosTotales':User.objects.all().order_by('id')
        })
    else:
        return HttpResponseRedirect(reverse('gestion_tienda : panelNavegacion'))

def eliminarUsuario(request,ind):
    usuarioEliminar = User.objects.get(id=ind)
    datosUsuario.objects.get(user=usuarioEliminar).delete()
    usuarioEliminar.delete()
    return HttpResponseRedirect(reverse('gestion_tienda:panelNavegacion'))

@login_required(login_url='http://127.0.0.1:8000')
def nuevoProducto (request):
    if request.method == 'POST':
        nombreProducto = request.POST.get('nombreProducto')
        codigoProducto = request.POST.get('codigoProducto')
        precioCompra = request.POST.get('precioCompra')
        precioVenta = request.POST.get('precioVenta')
        usernameUsuario = request.POST.get('usernameUsuario')

        productoNuevo = User.objects.create(
            nombreProducto = nombreProducto,
            codigoProducto = codigoProducto,
        )

        datosProducto.objects.create(
            precioCompra = precioCompra,
            precioVenta = precioVenta,
            username = usernameUsuario,
        )
        return HttpResponseRedirect(reverse('gestion_tienda : panelNavegacion'))
    return render(request,'panelNavegacion.html',{
        'productosTotales':User.objects.all().order_by('id')
    })

def eliminarProducto(request,ind):
        productoEliminar = User.objects.get(id=ind)
        datosProducto.objects.get(user=productoEliminar).delete()
        productoEliminar.delete()
        return HttpResponseRedirect(reverse('gestion_tienda:panelNavegacion'))