from django.db import models

# Create your models here.
class Producto(models.Model):

    descripcion = models.TextField()

    nombre_producto = models.CharField(max_length=40)

    stock = models.IntegerField()

    precio_unitario = models.IntegerField()

    categoria = models.CharField(max_length=20)


class Usuario(models.Model):

    usuario = models.CharField(max_length=30,unique=True)

    password = models.CharField(max_length=120)

    nombre = models.CharField(max_length=30)

    

class Pedidos(models.Model):

    numero_pedido = models.IntegerField()
    
    fecha_pedido = models.DateField(auto_now_add=True)
    
    monto = models.IntegerField()

    estado = models.CharField(max_length=20)

class Pedido_detalle(models.Model):

    id_pedido = models.ForeignKey(Pedidos,on_delete=models.CASCADE)

    id_producto = models.ForeignKey(Producto,on_delete=models.CASCADE)

    cantidad = models.IntegerField()

    monto = models.IntegerField()

    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

