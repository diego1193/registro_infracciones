from django.contrib import admin
from django.urls import path
from gestion_infracciones.views import LoginAPIView, GenerarInformeAPIView, login_view, informe_view
from gestion_infracciones.admin import my_admin_site
from infracciones.views import CargarInfraccionAPIView, CargarInfraccionView

urlpatterns = [
    path('admin/', my_admin_site.urls),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('carga_infraccion/', CargarInfraccionAPIView.as_view(), name='carga_infraccion'),
    path('generar_informe/<str:email>/', GenerarInformeAPIView.as_view(), name="generar_informe"),
    path('login_user/', login_view, name='login_user'),
    path('cargar_infraccion/', CargarInfraccionView.as_view(), name='cargar_infraccion'),
    path('informe/', informe_view, name='informe'),  # Añade la ruta a la vista
]
