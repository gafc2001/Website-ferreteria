from website.settings import USE_I18N
from django.contrib import admin

from pedido.models import *

admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Pedidos)
admin.site.register(Pedido_detalle)
