from django.urls import path
from . import views

app_name = 'clientes'
urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear_cliente, name='crear_cliente'),
    path('detalle/<int:id_cliente>', views.detalle, name='detalle'),
    path('cuentas/crear/<int:id_cliente>', views.crear_cuenta, name='crear_cuenta'),
    path('borrar/<int:id_cliente>', views.borrar_cliente, name='borrar_cliente'),
    path('cuentas/borrar/<int:id_cliente>/<int:id_cuenta>', views.borrar_cuenta, name='borrar_cuenta'),
]