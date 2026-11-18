from django.contrib import admin
from django.urls import path,include
from .views import HomeView, cerrarSesion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView,name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/',cerrarSesion,name='salir'),
    path('centrocostos/',include('centro_costos.urls', namespace='centro_costos')),
]