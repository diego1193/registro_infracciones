from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Persona, Vehiculo, Oficial
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class MyAdminSite(AdminSite):
    def has_permission(self, request):
        return request.user.is_active and request.user.is_superuser

my_admin_site = MyAdminSite(name='myadmin')

@admin.register(Persona, site=my_admin_site)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email")
    search_fields = ("nombre", "email")

@admin.register(Vehiculo, site=my_admin_site)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa_patente', 'marca', 'color', 'propietario')
    search_fields = ('placa_patente', 'marca')
    last_filter = ('marca', 'color')

@admin.register(Oficial, site=my_admin_site)
class OficialAdmin(admin.ModelAdmin):
    list_display = ("nombre", "numero_identificacion")
    search_fields = ("nombre", "numero_identificacion")

my_admin_site.register(User, UserAdmin)