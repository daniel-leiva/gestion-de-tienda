from lzma import MODE_FAST
from django.contrib import admin
from .models import *


# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "cui_empleado", "telefono",)

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "rubro", "producto_servicio", "direccion",)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "estado",)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("clave_producto", "nombre", "marca", "cantidad_ingreso", "precio", "proveedor_producto",)

class AsistenciaEmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre_empleado", "fecha_asistencia", "asistencia",)

class ConteoInventarioAdmin(admin.ModelAdmin):
    list_display = ("conteo_producto", "nombre_producto", "empleado_conteo",)



admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Asistencia_Empleado, AsistenciaEmpleadoAdmin)
admin.site.register(Conteo_Inventario, ConteoInventarioAdmin)

