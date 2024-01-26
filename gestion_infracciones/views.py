from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Persona, Vehiculo, Oficial
from infracciones.models import Infraccion
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

def login_view(request):
    # Maneja la solicitud POST para el inicio de sesión.
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)

        # Verifica si el usuario existe y pertenece al grupo 'oficiales'.
        if user is not None and Oficial.objects.filter(user=user).exists():
            login(request, user)

            # Genera tokens de acceso y refresco.
            refresh = RefreshToken.for_user(user)
            request.session['refresh'] = str(refresh)
            request.session['access'] = str(refresh.access_token)

            return redirect(reverse('cargar_infraccion'))
        else:
            # Si la autenticación falla, muestra un mensaje de error.
            messages.error(request, 'Credenciales incorrectas o no es un oficial')
            return redirect('login_user')

    # Renderiza la página de inicio de sesión para solicitudes GET.
    return render(request, 'login.html')


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Extrae el nombre de usuario y la contraseña de la solicitud.
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        # Autentica y genera tokens si el usuario es válido y es un oficial.
        if user and user is not None and Oficial.objects.filter(user=user).exists():
            refresh = RefreshToken.for_user(user)    
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token)
                },
                status=200
            )
        elif user:
            # Usuario no es un oficial.
            return Response({"error": "El usuario no es un oficial"}, status=403)
        else:
            # Autenticación fallida.
            return Response({"error": "Credenciales incorrectas"}, status=400)


class GenerarInformeAPIView(APIView):
    def get(self, request, email):
        try:
            # Busca una persona por email.
            persona = Persona.objects.get(email=email)
        except Persona.DoesNotExist:
            # Si no se encuentra, devuelve un error 404.
            return Response({"error": "Persona no encontrada"}, status=404)

        # Obtiene placas de vehículos asociados con la persona.
        placas_patentes = Vehiculo.objects.filter(propietario=persona).values_list("placa_patente", flat=True)
        # Obtiene infracciones asociadas con las placas.
        infracciones = Infraccion.objects.filter(placa_patente__in=placas_patentes)

        # Prepara los datos para la respuesta.
        data = [
            {
                "placa_patente": infraccion.placa_patente, 
                "timestamp": infraccion.timestamp, 
                "comentarios": infraccion.comentarios
            } 
            for infraccion in infracciones
        ]

        return Response(data)


def informe_view(request):
    # Renderiza la página para mostrar informes.
    return render(request, 'informe.html')