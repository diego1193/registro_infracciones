from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import InfraccionSerializer
from .forms import InfraccionForm
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from rest_framework_simplejwt.exceptions import InvalidToken
from django.contrib import messages


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class CargarInfraccionAPIView(APIView):
    """
    API View para cargar una nueva infracción.
    Requiere autenticación y que el usuario tenga permisos.
    """

    def post(self, request):
        """
        Maneja la solicitud POST para crear una nueva infracción.
        """
        serializer = InfraccionSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"mensaje": "Infracción registrada"}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CargarInfraccionView(LoginRequiredMixin, View):
    """
    Vista para cargar una nueva infracción desde la interfaz de usuario.
    Requiere que el usuario haya iniciado sesión.
    """

    def get(self, request, *args, **kwargs):
        """
        Muestra el formulario para cargar una nueva infracción.
        """
        form = InfraccionForm()
        return render(request, 'cargar_infraccion.html', {'form': form})

    def post(self, request, *args, **kwargs):
        """
        Procesa el formulario de infracción una vez enviado.
        """
        form = InfraccionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Infracción registrada con éxito')
            return redirect('cargar_infraccion')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
            return render(request, 'cargar_infraccion.html', {'form': form})


