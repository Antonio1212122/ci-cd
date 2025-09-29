from django.db import models

# Modelo para almacenar información de estudiantes
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    carrera = models.CharField(max_length=100)
    promedio = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.matricula})"

# Modelo para almacenar hitos (eventos importantes, como CI/CD)
class Hito(models.Model):
    titulo = models.CharField(max_length=200)  # Título del hito
    descripcion = models.TextField()           # Descripción del hito
    fecha = models.DateField(auto_now_add=True)  # Fecha de creación automática

    def __str__(self):
        return self.titulo