from django.http import HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from .models import Tarea


# Create your views here.
def listar_tareas(request):
    print(request.user)
    if not request.user.is_authenticated or request.user.is_anonymous:
        return HttpResponseRedirect(reverse('authentication:login_view'))
    tareas = Tarea.objects.all()
    context = {'lista_tareas': tareas}
    return render(request, 'lista_tareas/index.html', context)


def crear_tarea(request):
    tarea = Tarea(
        texto=request.POST['texto'],
        prioridad=int(request.POST['prioridad']),
        fecha_creacion=timezone.now()
    )
    tarea.save()
    return HttpResponseRedirect(reverse('lista_tareas:listar_tareas'))


def eliminar_tarea(request, id_tarea):
    tarea = get_object_or_404(Tarea, pk=id_tarea)
    tarea.delete()
    return HttpResponseRedirect(reverse('lista_tareas:listar_tareas'))
