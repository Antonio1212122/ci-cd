from django.urls import path, include
from rest_framework import routers
from .views import EstudianteViewSet  # Importa el ViewSet de estudiantes
from . import views  # Importa manualmente el módulo views para acceder a sus funciones

# Router para las vistas basadas en ViewSet (estudiantes)
router = routers.DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet)

# Definición de rutas de la app API
urlpatterns = [
    # Rutas automáticas para estudiantes (GET, POST, PUT, DELETE)
    path('', include(router.urls)),
    # Ruta para listar y crear hitos (GET y POST)
    path('hitos/', views.hito_list_create, name='hito-list-create'),
]