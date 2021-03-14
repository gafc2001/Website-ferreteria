from pedido import models
from django.shortcuts import render
from django.http import HttpResponse, response
from pedido.models import *
import json

def listar_pedido(request):
    
    pedido = Pedidos.objects.all()
    
    

    return render(request,'pedido.html',{'data':pedido})


def home(request):
    
    productos = Producto.objects.all()
    return render(request,'index.html',{'productos':productos})

def detalles(request,id):
    

    details = Pedido_detalle.objects.filter(id_pedido_id= int(id))
    pedido = Pedidos.objects.get(id=id)
    for detail in details:
        detail.id_producto_id = Producto.objects.get(id=detail.id_producto_id)


    return render(request,'detalles.html',{'details':details,'pedido':pedido})

def compra(request):
    respuesta = request.POST

    response_data = respuesta['data']
    arreglo = response_data.split('},')
    pedidos = []
    for element in arreglo:
        if (element[-1] != '}'):
            element = element + '}'
        pedidos.append(json.loads(element))
    
    total = 0
    for producto in pedidos:
        query_producto = Producto.objects.get(id = producto['id'])
        producto['nombre_producto'] = query_producto.nombre_producto
        producto['precio_unitario'] = query_producto.precio_unitario
        producto['descripcion'] = query_producto.descripcion
        producto['monto'] = producto['precio_unitario'] * producto['cant']
        producto['img'] = query_producto.img
        total += producto['monto']
        #Reduciendo el stock
        #query_producto.stock = int(query_producto.stock) - producto.cant
    return render(request,'compra.html',{'pedidos':pedidos,'total':total})

def envio(request):
    respuesta = request.POST
    response_data = respuesta['data']
    var=response_data[1:-1]
    arreglo = var.split('},')
    pedidos = []
    for element in arreglo:
        if (element[-1] != '}'):
            element = element + '}'
        pedidos.append(json.loads(element))
    
    total = 0
    cantidad=0
    for producto in pedidos:
        query_producto = Producto.objects.get(id = producto['id'])

        producto['precio_unitario'] = query_producto.precio_unitario
        producto['monto'] = producto['precio_unitario'] * producto['cant']
        total += producto['monto']
        cantidad += producto['cant']

    Pedidos.objects.create( numero_pedido=cantidad,monto=total,estado="NO ENTREGADO")
#    if form.is_valid():
#      form.save()
#      return redirect('detalles')
# cambio
    
    return render(request,'compra.html',{"mensaje":'OK'})
        
