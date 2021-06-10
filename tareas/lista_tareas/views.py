from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from .models import Cliente, Tarea
from .forms import CrearTareaForm, ClienteForm


@login_required
def listar_tareas(request):
    print(request.user.has_perm('lista_tareas.add_tarea'))
    tareas = Tarea.objects.all()
    context = {
        'lista_tareas': tareas,
        'crear_form': CrearTareaForm()
        }
    return render(request, 'lista_tareas/index.html', context)


#                       nombre_app.permiso([add, change, delete, view]_{modelo})
@permission_required('lista_tareas.add_tarea')
def crear_tarea(request):
    form = CrearTareaForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        tarea = Tarea(
            texto=form.cleaned_data['texto'],
            prioridad=form.cleaned_data['prioridad'],
            fecha_creacion=timezone.now()
        )
        tarea.save()
    
    return HttpResponseRedirect(reverse('lista_tareas:listar_tareas'))


def eliminar_tarea(request, id_tarea):
    tarea = get_object_or_404(Tarea, pk=id_tarea)
    tarea.delete()
    return HttpResponseRedirect(reverse('lista_tareas:listar_tareas'))


def clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('lista_tareas:clientes'))
    else:
        clientes = Cliente.objects.all()
        form = ClienteForm()
        context = {
            'clientes': clientes,
            'form': form
        }
        return render(request, 'lista_tareas/clientes.html', context)