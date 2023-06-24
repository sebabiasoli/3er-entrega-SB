from django import forms

class IniciarCompraFormulario(forms.Form):
    articulo = forms.CharField(max_length=30)
    precio = forms.IntegerField()
    fecha_de_oferta = forms.DateField(required=False)