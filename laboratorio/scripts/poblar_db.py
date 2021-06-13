from django.contrib.auth.models import User
from inventario.models import Encargado, Categoria

lista_encargados = [
    {'nombre': 'Juan Perez', 'carrera': 'ETN'},
    {'nombre': 'Sara Rivera', 'carrera': 'MEC'},
    {'nombre': 'Maria Antelo', 'carrera': 'TEL'},
    {'nombre': 'Sandra Manrique', 'carrera': 'ETN'},
]

lista_categorias = [
    'instrumentos de medicion',
    'herramientas',
    'placas de desarrollo',
    'actuadores',
    'sensores',
    'material de oficina',
]


def crear_usuarios():
    User.objects.create_superuser(username='admin', email='a@d.min', password='admin')


def crear_encargados():
    for encargado_dic in lista_encargados:
        encargado = Encargado(**encargado_dic)
        encargado.save()


def crear_categorias():
    for cat in lista_categorias:
        categoria = Categoria(nombre=cat)
        categoria.save()


def run():
    crear_categorias()
    crear_encargados()
    crear_usuarios()
