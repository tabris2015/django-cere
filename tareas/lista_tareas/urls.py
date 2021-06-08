from django.urls import path
from . import views


app_name = 'lista_tareas'
urlpatterns = [
    path('', views.listar_tareas, name='listar_tareas'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
    path('eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
]
