from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from .models import Cliente, Cuenta


# Create your views here.
def index(request):
    """Desplegar todos los clientes"""
    # obtener clientes de la DB
    clientes = Cliente.objects.all()
    context = {'lista_clientes': clientes}

    return render(request, 'clientes/index.html', context)


def crear_cliente(request):
    nombre = request.POST['nombre']
    nuevo_cliente = Cliente(nombre=nombre, fecha_registro=timezone.now())
    nuevo_cliente.save()
    return HttpResponseRedirect(reverse('clientes:index'))


def detalle(request, id_cliente):
    # verificar si el cliente existe
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    # print('cuentas:', cliente.cuenta_set.count())
    cuentas = cliente.cuenta_set.all()
    context = {'cliente': cliente, 'lista_cuentas': cuentas}
    return render(request, 'clientes/detalle.html', context)


def crear_cuenta(request, id_cliente):
    categoria = request.POST['categoria']
    # verificar si el cliente existe
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    cuenta = Cuenta(categoria=categoria, cliente=cliente)
    cuenta.save()
    return HttpResponseRedirect(reverse('clientes:detalle', args=[id_cliente]))


def borrar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    cliente.delete()    # se elimina de la DB
    return HttpResponseRedirect(reverse('clientes:index'))


def borrar_cuenta(request, id_cliente, id_cuenta):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    cuenta = get_object_or_404(Cuenta, pk=id_cuenta)
    cuenta.delete()
    return HttpResponseRedirect(reverse('clientes:detalle', args=[id_cliente]))