from pedido import models
from django.shortcuts import render
from django.http import HttpResponse, response
from pedido.models import *
import json

def listar_pedido(request):
    
    pedido = Pedidos.objects.all()
    
    

    return render(request,'pedido.html',{'data':pedido})


def home(request):
    return render(request,'index.html')

def detalles(request,id):
    

    details = Pedido_detalle.objects.filter(id_pedido_id= int(id))
    pedido = Pedidos.objects.get(id=id)
    for detail in details:
        detail.id_producto_id = Producto.objects.get(id=detail.id_producto_id)


    return render(request,'detalles.html',{'details':details,'pedido':pedido})

def compra(request):
    respuesta = request.POST

    json_data = respuesta['data']
    diccionario = json.loads(json_data)
    return render(request,'compra.html',{'data':diccionario['1']})
