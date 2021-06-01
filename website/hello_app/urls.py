from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('saludo', views.saludo, name='saludo'),
    path('not_found', views.not_found, name='not_found'),
    path('bad_request', views.bad_request, name='bad_request'),
    # http://localhost:8000/hello/saludo_edad/90
    path('saludo_edad/<int:edad>/<str:nombre>', views.saludo_edad, name='saludo_edad'),  
    path('estudiante/<str:nombre>', views.estudiante, name='estudiante'),
]