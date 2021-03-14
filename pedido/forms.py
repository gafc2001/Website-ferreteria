from django import forms
from .models import Pedidos

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = '__all__'