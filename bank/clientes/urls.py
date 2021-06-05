from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('crear/<str:nombre>', views.crear_cliente, name='crear_cliente'),
    path('detalle/<int:id_cliente>', views.detalle, name='detalle'),
    path('cuentas/crear/<int:id_cliente>/<str:categoria>', views.crear_cuenta, name='crear_cuenta'),
]