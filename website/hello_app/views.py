from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.decorators.http import require_http_methods, require_GET
from time import sleep

@require_GET
def index(request):
    sleep(0.05)
    return HttpResponse('<h1>hola bola!</h1>')

# @require_http_methods(['POST', 'PUT'])
def saludo(request):
    print('ejecutando el saludo...')
    return HttpResponse('<h2>hola a todos!</h2><br>esto es html!')

def not_found(request):
    # return HttpResponseNotFound('no existe')
    raise Http404('no existe')

def bad_request(request):
    return HttpResponse('error', status=400)

def saludo_edad(request, edad, nombre):
    if edad > 18:
        return HttpResponse(f'ya puedes comprar alcohol {nombre}')
    else:
        return HttpResponse(f'eres muy joven {nombre}', status=403)
    

def estudiante(request, nombre):
    params = request.GET
    if 'mat' not in params or 'qmc' not in params or 'fis' not in params:
        return HttpResponse('no hay notas', status=400)
    print(params)
    try:
        mat = int(params['mat'])
        qmc = int(params['qmc'])
        fis = int(params['fis'])
    except ValueError as e:
        return HttpResponse('datos invalidos', status=422)

    promedio = (mat + fis + qmc) / 3
    return HttpResponse(f'hola {nombre} <br> su promedio es {promedio:.2f}')
