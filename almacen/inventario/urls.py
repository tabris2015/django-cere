from django.urls import path
from . import views


app_name = 'inventario'
urlpatterns = [
    path('items/', views.items, name='items'),
]
