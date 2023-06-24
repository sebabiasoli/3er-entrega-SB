from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('iniciar_compra/', views.iniciar_compra, name='iniciar_compra')
]
