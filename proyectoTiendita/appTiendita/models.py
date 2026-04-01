from os import truncate
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.

class Empleado(models.Model):
    """Modelo para guardar los datos del empleado"""

    MASCULINO = "M"
    FEMENINO = "F"
    OTRO = "O"

    OPCIONES_SEXO = (
        (MASCULINO, "Masculino"),
        (FEMENINO, "Femenino"),
        (OTRO, "Otro"),
    )

    nombre = models.CharField(max_length=20, blank=False, null=False)
    apellido = models.CharField(max_length=20, blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    lugar_residencia = models.CharField(max_length=20, blank=False, null=False)
    cui_empleado = models.CharField(max_length=13, blank=False, null=False)
    sexo_empleado = models.CharField(max_length=1, choices=OPCIONES_SEXO, blank=False, null=False)
    telefono = models.CharField(max_length=8, blank=False, null=False)

    class Meta:
        db_table = "Empleados"
        verbose_name_plural = "Datos de los Empleados"
    
    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido)



class Proveedor(models.Model):
    """Modelo para guardar datos de los proveedores"""

    nombre = models.CharField(max_length=40, blank=False, null=False)
    telefono = models.CharField(max_length=8, blank=False, null=False)
    direccion = models.CharField(max_length=40, blank=False, null=False)
    rubro = models.CharField(max_length=20, blank=False, null=False)
    producto_servicio = models.CharField(max_length=50, blank=False, null=False)
    

    class Meta:
        db_table = "Proveedores"
        verbose_name_plural = "Datos de los Proveedores"
    
    def __str__(self):
        return str(self.nombre)



class Cliente(models.Model):
    """Modelo para guardar datos de los Clientes"""

    ACTIVO = "A"
    INACTIVO = "I"

    ESTADO_CLIENTE = (
        (ACTIVO, "Activo"),
        (INACTIVO, "Inactivo"),
    )

    nombre = models.CharField(max_length=50, blank=False, null=False)
    telefono = models.CharField(max_length=8, blank=False, null=False)
    nit_cliente = models.CharField(max_length=13, blank=False, null=False)
    lugar_residencia = models.CharField(max_length=30, blank=False, null=False)
    estado = models.CharField(max_length=1, choices=ESTADO_CLIENTE, blank=False, null=False)

    class Meta:
        db_table = "Clientes"
        verbose_name_plural = "Datos de los Clientes"

    def __str__(self):
        return str(self.nombre)



class Producto(models.Model):
    """Modelo para guardar los Productos"""

    DISPONIBLE = "D"
    NO_DISPONIBLE = "N"

    ESTADO_PRODUCTO = (
        (DISPONIBLE, "Disponible"),
        (NO_DISPONIBLE, "No disponible"),
    )

    nombre = models.CharField(max_length=30, blank=False, null=False)
    marca = models.CharField(max_length=20, blank=False, null=False)
    cantidad_ingreso = models.IntegerField(validators=[MaxValueValidator(100)], blank=False, null=False)
    clave_producto = models.AutoField(primary_key=True, blank=False, null=False)
    precio = models.DecimalField(decimal_places=2, max_digits=5)
    disponibilidad = models.CharField(max_length=1, choices=ESTADO_PRODUCTO, blank=False, null=False, default=DISPONIBLE)
    proveedor_producto = models.ForeignKey(Proveedor, on_delete=models.PROTECT, default=1)

    class Meta:
        db_table = "Productos"
        verbose_name_plural = "Listado de los Productos"

    def __str__(self):
        return str(self.nombre)



class Asistencia_Empleado(models.Model):
    """Modelo para registrar la Asistencia de los Empleados"""

    SI_ASISTIO = "1"
    NO_ASISTIO = "0"

    ESTADO_ASISTENCIA = (
        (SI_ASISTIO, "Si asistió"),
        (NO_ASISTIO, "No asistió"),
    )

    asistencia = models.CharField(max_length=1, choices=ESTADO_ASISTENCIA, blank=False, null=False)
    fecha_asistencia = models.DateTimeField(auto_now_add=True)
    nombre_empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)

    class Meta:
        db_table = "Asistencia Empleados"
        verbose_name_plural = "Asistencia de los Empleados"

    def __str__(self):
        return str(self.nombre_empleado)



class Conteo_Inventario(models.Model):
    """Modelo para verificación de productos en el Inventario"""

    conteo_producto = models.IntegerField(validators=[MaxValueValidator(100)], blank=False, null=False)
    nombre_producto = models.ForeignKey(Producto, on_delete=models.PROTECT, default=None)
    empleado_conteo = models.ForeignKey(Empleado, on_delete=models.PROTECT, default=None)
    

    class Meta:
        db_table = "Conteo Inventario"
        verbose_name_plural = "Registros del Inventario"
    
    def __str__(self):
        return str(self.nombre_producto)

