from django.shortcuts import render, redirect
from inicio.forms import IniciarVentaFormulario, IniciarCompraFormulario, BuscarArticulo
from inicio.models import Vender, Comprar


# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def articulos_en_venta(request):
    
    formulario = BuscarArticulo(request.GET)
    if formulario.is_valid():
        articulo_a_buscar = formulario.cleaned_data['articulo']
        listado_de_articulos = Vender.objects.filter(articulo__icontains=articulo_a_buscar)
   
    formulario = BuscarArticulo()    
    return render(request, 'inicio/articulos_en_venta.html', {'formulario': formulario, 'articulos':listado_de_articulos})


def iniciar_venta(request):
    mensaje = ''
    if request.method == 'POST':
        forumulario = IniciarVentaFormulario(request.POST)
        if forumulario.is_valid():
            info = forumulario.cleaned_data
            venta = Vender(articulo=info['articulo'],precio=info['precio'],fecha_de_oferta=info['fecha_de_oferta'])
            venta.save()
            return redirect('inicio:articulos_en_venta')
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
    
    
    
