from rest_framework import serializers
from .models import Estudiante, Hito

# Serializer para el modelo Estudiante (convierte objetos a JSON y viceversa)
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

# Serializer para el modelo Hito (convierte objetos a JSON y viceversa)
class HitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hito
        fields = '__all__'