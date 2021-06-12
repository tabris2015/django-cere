from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from .views import ItemView, CategoriaView, EncargadosListView, ItemDetailView, EncargadoDetailView


app_name = 'inventario'
urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='inventario/index.html'),
        name='index'
    ),
    path(
        'items/',
        login_required(ItemView.as_view()),
        name='items'
    ),
    path(
        'categorias/',
        permission_required('inventario.add_categoria')(CategoriaView.as_view()),
        name='categorias'
    ),
    path(
        'encargados/',
        EncargadosListView.as_view(),
        name='encargados'
    ),
    path(
        'items/detalle/<slug:slug>/',
        ItemDetailView.as_view(),
        name='detalle_item'
    ),
    path(
        'encargados/detalle/<slug:slug>/',
        EncargadoDetailView.as_view(),
        name='detalle_encargado'
    ),
]
