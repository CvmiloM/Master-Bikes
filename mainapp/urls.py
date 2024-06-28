from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.clientes, name='clientes'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('solicitud/<int:solicitud_id>/', views.detalle_solicitud, name='detalle_solicitud'),
    path('solicitud/<int:solicitud_id>/confirmar/', views.confirmar_solicitud, name='confirmar_solicitud'),
    path('solicitud/<int:solicitud_id>/rechazar/', views.rechazar_solicitud, name='rechazar_solicitud'),
    # Elimina esta línea si no necesitas la funcionalidad enviar_correo
    # path('solicitud/<int:solicitud_id>/enviar-correo/', views.enviar_correo, name='enviar_correo'),
    path('historial/', views.historial, name='historial'),
]
