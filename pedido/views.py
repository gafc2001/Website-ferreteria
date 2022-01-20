from pedido import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from django.contrib.auth.hashers import make_password
from pedido.models import *
import json
import random
from django.contrib.auth.decorators import login_required

def home(request):

    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

@login_required
def listar_pedido(request):

    id = request.session['id']
    pedido = ''
    msg = ''
    try:
        pedido = Pedidos.objects.filter(id_usuario_id=id)
    except:
        msg = "No tienes pedidos aún, compra con nosotros ahora!"
    
    return render(request, 'pedido.html', {'data': pedido, 'msg': msg})

@login_required
def detalles(request, id):

    details = Pedido_detalle.objects.filter(id_pedido_id=id)
    pedido = Pedidos.objects.get(id=id)
    for detail in details:
        detail.id_producto_id = Producto.objects.get(id=detail.id_producto_id)

    return render(request, 'detalles.html', {'details': details, 'pedido': pedido})

@login_required
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
        query_producto = Producto.objects.get(id=producto['id'])
        producto['nombre_producto'] = query_producto.nombre_producto
        producto['precio_unitario'] = query_producto.precio_unitario
        producto['descripcion'] = query_producto.descripcion
        producto['monto'] = producto['precio_unitario'] * producto['cant']
        producto['img'] = query_producto.img
        total += producto['monto']
        # Reduciendo el stock
        #query_producto.stock = int(query_producto.stock) - producto.cant

    formatPedidos = str(pedidos)[1:-1]

    return render(request, 'compra.html', {'pedidos': pedidos, 'strPedidos': formatPedidos, 'total': total})

@login_required
def envio(request):
    respuesta = request.POST
    data = respuesta['data'].replace("\'", '\"')
    arreglo = data.split("},")
    pedidos = []
    for element in arreglo:
        if (element[-1] != "}"):
            element = element + '}'
        pedidos.append(json.loads(element))

    total = respuesta['monto']
    id = request.session['id']
    # Guardando pedido

    numPedido = random.randint(100000, 999999)
    pedido = Pedidos.objects.create(numero_pedido=str(
        numPedido), monto=total, estado="NO ENTREGADO", id_usuario_id=id)

    # Guardando detalles
    for pedido_detalle in pedidos:
        data = {
            'cantidad': pedido_detalle['cant'],
            'monto': pedido_detalle['monto'],
            'id_pedido_id': pedido.id,
            'id_producto_id': pedido_detalle['id'],
        }
        detalles = Pedido_detalle.objects.create(**data)

    return redirect('pedido')


def iniciarSesionView(request):
    return render(request, 'login.html')


def procesarLogin(request):
    form = request.POST
    usuario = form['user']
    password = form['password']
    user = authenticate(username=usuario, password=password)

    if (user is not None):
        request.session['id'] = user.id
        request.session['username'] = user.username
        request.session['nombre'] = user.first_name
        return redirect('home')
    else:
        return render(request, 'login.html', {'mensaje': 'Credenciales inválidas'})


def registrarUsuarioView(request):
    return render(request, 'registroUsuario.html')


def registrarUsuario(request):
    form = request.POST
    usuario = form['user']
    password = form['password']
    nombre = form['nombre']
    correo = form['correo']

    user = User.objects.create(
        username=usuario, email=correo, password=make_password(password), first_name=nombre)

    if (user is not None):
        request.session['id'] = user.id
        request.session['username'] = user.username
        request.session['nombre'] = user.first_name
        return redirect('home')

    else:
        return render(request, 'registroUsuario.html', {'mensaje': 'Error al registrar'})

@login_required
def close_session(request, msg):
    if(msg == 'close'):
        del request.session['id']
        del request.session['username']
        del request.session['nombre']
        return redirect('home')

def handle_404_error(request,exception):
    return render(request, '404.html')
