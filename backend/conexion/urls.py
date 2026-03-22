from django.urls import path
from .views import CrearSala

urlpatterns = [
    path('crearSala/', CrearSala.as_view(), name='conexion')
]