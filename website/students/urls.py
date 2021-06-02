from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # crear estudiante /students/crear/<nombre>
    path('crear/<str:nombre>', views.crear_estudiante, name='crear_estudiante'),
    path('notas/<str:nombre>', views.crear_estudiante_notas, name='crear_notas'),
    path('<str:nombre>/promedio', views.promedio_estudiante, name='promedio'),
]