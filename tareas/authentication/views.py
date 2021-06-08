from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate


# Create your views here.
def login_user(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('lista_tareas:listar_tareas'))
    else:
        return HttpResponse('no existe', status=403)


def login_view(request):
    return render(request, 'authentication/login.html')
