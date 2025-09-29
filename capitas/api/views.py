from rest_framework import viewsets
from .models import Estudiante, Hito
from .serializers import EstudianteSerializer, HitoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# ViewSet para operaciones CRUD sobre estudiantes (usa routers)
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

# Vista basada en función para listar (GET) y crear (POST) hitos
@api_view(['GET', 'POST'])
def hito_list_create(request):
    """
    GET: Devuelve la lista de todos los hitos registrados.
    POST: Crea un nuevo hito con los datos proporcionados.
    """
    if request.method == 'GET':
        hitos = Hito.objects.all()
        serializer = HitoSerializer(hitos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HitoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)