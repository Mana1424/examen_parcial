from django.contrib.auth.models import User
from django.db import models
from datetime import date

class datosUsuario(models.Model):
    nombreUsuario = models.CharField(max_length=30)
    apellidoUsuario = models.CharField(max_length=30)
    emailUsuario = models.EmailField(unique=True)
    user = models.OneToOneField (User, on_delete=models.CASCADE)
    contraUsuario = models.OneToOneField (User, on_delete=models.CASCADE)
    tipoUsuario = models.CharField(max_length=20, default='VENDEDOR')
    nroCelular = models.CharField(max_length=15)
    fechaIngreso = models.DateTimeField(default=date.today)

class datosProducto(models.Model):
    usuarioRelacionado = models.ForeignKey(User, on_delete=models.CASCADE)
    nombreProducto = models.CharField(max_length=100)
    codigoProducto = models.CharField(max_length=50)
    precioCompra = models.DecimalField(max_digits=10, decimal_places=2)
    precioVenta = models.DecimalField(max_digits=10, decimal_places=2)

