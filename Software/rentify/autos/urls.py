from django.urls import path
from . import views

urlpatterns = [
    # Página de inicio
    path('', views.inicio, name='inicio'),

    # CRUD de Autos
    path('autos/', views.lista_autos, name='lista_autos'),
    path('autos/crear/', views.crear_auto, name='crear_auto'),
    path('autos/<int:pk>/', views.detalle_auto, name='detalle_auto'),
    path('autos/<int:pk>/editar/', views.editar_auto, name='editar_auto'),
    path('autos/<int:pk>/eliminar/', views.eliminar_auto, name='eliminar_auto'),
]
