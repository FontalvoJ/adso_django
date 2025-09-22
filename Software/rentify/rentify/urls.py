from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Incluir todas las rutas de la app autos (inicio + CRUD)
    path('', include('autos.urls')),
]
