
from django.contrib import admin
from django.urls import path
from empresa.viewsets import crear_empresa, actualizar_empresa, eliminar_empresa, listar_empresas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear/', crear_empresa, name="Metodo crear ( POST ), para la creacion de una nueva empresa"),
    path('listar/', listar_empresas, name="Metodo para obtener empresas (GET)"),
    path('actualizar/<int:id>/', actualizar_empresa, name="Metodo para actualizar un registro (PUT)"), 
    path('eliminar/<int:id>/', eliminar_empresa, name="Metodo para eliminar un registro (DELETE)")
]
