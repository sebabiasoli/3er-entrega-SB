from django.shortcuts import render
from inicio.forms import IniciarCompraFormulario
from inicio.models import Comprar
# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')


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
    
    
    
    
# def iniciar_compra(request):
#     mensaje = ''
    
#     if request.method == 'POST':
#         formulario = IniciarCompraFormulario(request.POST)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             Compra = Comprar(artiulo=info['articulo'],precio=info['precio'],fecha_de_oferta=info['fecha_de_oferta'])
#             Compra.save()
#             mensaje = f'Se relizo la oferta {Compra.artiulo}'
#         else:
#             return render(request, 'inicio/iniciar_compra.html', {'formulario': formulario})
    
#     formulario = IniciarCompraFormulario()
#     return render(request, 'inicio/iniciar_compra.html', {'formulario': formulario, 'mensaje': mensaje})