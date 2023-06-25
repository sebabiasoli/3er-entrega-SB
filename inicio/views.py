from django.shortcuts import render
from inicio.forms import IniciarVentaFormulario, IniciarCompraFormulario
from inicio.models import Vender, Comprar


# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')


def iniciar_venta(request):
    mensaje = ''
    if request.method == 'POST':
        forumulario = IniciarVentaFormulario(request.POST)
        if forumulario.is_valid():
            info = forumulario.cleaned_data
            venta = Vender(articulo=info['articulo'],precio=info['precio'],fecha_de_oferta=info['fecha_de_oferta'])
            venta.save()
            mensaje = f'Se realizo la compra de {venta.articulo} al valor de USD {venta.precio}'            
        else:
            return render(request, 'inicio/iniciar_venta.html', {'formulario': forumulario})
    forumulario = IniciarVentaFormulario()
    return render(request, 'inicio/iniciar_venta.html', {'formulario': forumulario, 'mensaje':mensaje})
    
    
def iniciar_compra(request):
    mensaje = ''
    if request.method == 'POST':
        forumulario = IniciarCompraFormulario(request.POST)
        if forumulario.is_valid():
            info = forumulario.cleaned_data
            compra = Comprar(articulo=info['articulo'],precio=info['precio'],fecha_de_oferta=info['fecha_de_oferta'])
            compra.save()
            mensaje = f'Se realizo la compra de {compra.articulo} al valor de USD {compra.precio}'            
        else:
            return render(request, 'inicio/iniciar_compra.html', {'formulario': forumulario})
    forumulario = IniciarCompraFormulario()
    return render(request, 'inicio/iniciar_compra.html', {'formulario': forumulario, 'mensaje':mensaje})
    
    
    
