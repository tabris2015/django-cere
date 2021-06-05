from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Cliente, Cuenta


# Create your views here.
def index(request):
    """Desplegar todos los clientes"""
    # obtener clientes de la DB
    clientes = Cliente.objects.all()
    context = {'lista_clientes': clientes}

    return render(request, 'clientes/index.html', context)


def crear_cliente(request, nombre):
    nuevo_cliente = Cliente(nombre=nombre, fecha_registro=timezone.now())
    nuevo_cliente.save()
    return HttpResponse('cliente creado!', status=201)


def detalle(request, id_cliente):
    # verificar si el cliente existe
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    # print('cuentas:', cliente.cuenta_set.count())
    cuentas = cliente.cuenta_set.all()
    context = {'cliente': cliente, 'lista_cuentas': cuentas}
    return render(request, 'clientes/detalle.html', context)


def crear_cuenta(request, id_cliente, categoria):
    # verificar si el cliente existe
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    cuenta = Cuenta(categoria=categoria, cliente=cliente)
    cuenta.save()
    return HttpResponse('cuenta creada!', status=201)