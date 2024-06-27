from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('resuelto', 'Resuelto'),
        ('rechazado', 'Rechazado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado_actual = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.cliente.nombre}"

class HistorialReparacion(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    descripcion = models.TextField()
    repuestos_utilizados = models.TextField()
    tecnico = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Reparación {self.id} - {self.solicitud.cliente.nombre}"
