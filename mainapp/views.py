from django.shortcuts import render, get_object_or_404, redirect
from .models import Solicitud, Cliente, HistorialReparacion
from .forms import ConfirmarSolicitudForm, ClienteForm
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import Cliente, Solicitud

def home(request):
    return render(request, 'mainapp/home.html')
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'mainapp/clientes.html', {'clientes': clientes})


def solicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'mainapp/solicitudes.html', {'solicitudes': solicitudes})

def detalle_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    if request.method == 'POST':
        form = ConfirmarSolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            solicitud = form.save()
            # Enviar correo electrónico
            if solicitud.estado_actual == 'resuelto':
                asunto = 'Confirmación de reparación'
                mensaje = f'Hola {solicitud.cliente.nombre},\n\nTu bicicleta puede ser reparada. Nos pondremos en contacto contigo pronto.'
            else:
                asunto = 'Rechazo de reparación'
                mensaje = f'Hola {solicitud.cliente.nombre},\n\nLamentamos informarte que tu bicicleta no puede ser reparada.'
            send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [solicitud.cliente.email], fail_silently=False)
            return redirect('solicitudes')
    else:
        form = ConfirmarSolicitudForm(instance=solicitud)
    return render(request, 'mainapp/detalle_solicitud.html', {'solicitud': solicitud, 'form': form})

# Definición de otras vistas aquí

def confirmar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    if request.method == 'POST':
        solicitud.estado_actual = 'resuelto'
        solicitud.save()
        send_mail(
            'Confirmación de reparación',
            f'Hola {solicitud.cliente.nombre},\n\nTu bicicleta puede ser reparada. Nos pondremos en contacto contigo pronto.',
            settings.EMAIL_HOST_USER,
            ['tomas.leon.cisternas@gmail.com'],
            fail_silently=False,
        )
        return redirect('solicitudes')
    return render(request, 'mainapp/confirmar_solicitud.html', {'solicitud': solicitud})

def rechazar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    if request.method == 'POST':
        solicitud.estado_actual = 'rechazado'
        solicitud.save()
        send_mail(
            'Rechazo de reparación',
            f'Hola {solicitud.cliente.nombre},\n\nLamentamos informarte que tu bicicleta no puede ser reparada.',
            settings.EMAIL_HOST_USER,
            ['ca.monge@duocuc.cl'],
            fail_silently=False,
        )
        return redirect('solicitudes')
    return render(request, 'mainapp/rechazar_solicitud.html', {'solicitud': solicitud})

#send_email

def send_email(email):
    send_mail(
        'Confirmación de reparación'
    )


# Elimina o agrega la definición de enviar_correo si es necesario


