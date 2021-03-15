"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pedido import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pedido/',views.listar_pedido,name='pedido'),
    path('pedido/detalles/<int:id>',views.detalles, name='detalles'),
    path('',views.home,name='home'),
    path('compra/',views.compra,name='compra'),
    path('envio/',views.envio,name='envio'),
    
    path('wlogin/', views.iniciarSesionView, name='wlogin'),
    path('wregistrarUsuario/', views.registrarUsuarioView, name='wregistrarUsuario'),
    path('registrarUsuario/', views.registrarUsuario, name='registrarUsuario'),
    path('login/', views.procesarLogin, name='login'), 
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
