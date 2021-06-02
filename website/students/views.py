from django import http
from django.shortcuts import render
from django.http import HttpResponse


estudiantes = []

# Create your views here.
def index(request):
    estudiantes_html = '<ol>'
    for estudiante in estudiantes:
        estudiantes_html += f'<li>{estudiante["nombre"]}: {str(estudiante["notas"])}</li>'

    estudiantes_html += '</ol>'

    return HttpResponse(estudiantes_html)


def crear_estudiante(request, nombre):
    """Crear estudiante"""
    # crear diccionario con los datos del estudiante
    estudiante = {'nombre': nombre}
    # agregar estudiante a la DB
    estudiantes.append(estudiante)

    # devolver response 201 CREATED
    return HttpResponse(f'estudiante {nombre} creado!', status=201)


def crear_estudiante_notas(request, nombre):
    params = request.GET
    if not params:
        return HttpResponse('no hay notas', status=400)
    print(params)

    # for i in range(len(estudiantes)):
    #    estudiantes[i]
    id_estudiante = None
    for idx, estudiante in enumerate(estudiantes):
        if estudiante['nombre'] == nombre:
            id_estudiante = idx
            break
    
    # buscar el indice del estudiante
    if id_estudiante is None:
        estudiantes.append({'nombre': nombre})
        id_estudiante = len(estudiantes) - 1

    # agregar el diccionario de notas al estudiante correspondiente
    nuevo_estudiante = {
        'nombre': nombre,
        'notas': params.dict()
    }

    # reemplazar en la lista
    estudiantes[id_estudiante] = nuevo_estudiante

    # promedio = (mat + fis + qmc) / 3
    return HttpResponse(f'notas de {nombre} agregadas')


def promedio_estudiante(request, nombre):
    id_estudiante = None
    for idx, estudiante in enumerate(estudiantes):
        if estudiante['nombre'] == nombre:
            id_estudiante = idx
            break
    
    # buscar el indice del estudiante
    if id_estudiante is None:
        return HttpResponse(f'estudiante {nombre} no existe', status=404)

    acumulado = 0
    for materia, nota_str in estudiantes[id_estudiante]['notas'].items():
        acumulado += int(nota_str)
    
    promedio = acumulado / len(estudiantes[id_estudiante]['notas'])

    return HttpResponse(f'Promedio para {nombre}: {promedio:.2f}')
