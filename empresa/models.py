from django.db import models

class empresa(models.Model):
    id = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=100, verbose_name="direccion de la empresa")
    nombreEmpresa = models.CharField(max_length=200,verbose_name="nombre de la empresa")
    telefonoEmpresa = models.BigIntegerField(verbose_name="telefono de la empresa")
    nit = models.CharField(max_length=20, verbose_name="NIT de la empresa")
