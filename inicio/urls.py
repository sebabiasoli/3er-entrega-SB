from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('articulos_en_venta/', views.articulos_en_venta, name='articulos_en_venta'),
    path('iniciar_venta/', views.iniciar_venta, name='iniciar_venta'),
    path('iniciar_compra/', views.iniciar_compra, name='iniciar_compra')
]
