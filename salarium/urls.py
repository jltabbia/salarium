from django.contrib import admin
from django.urls import path,include
from .views import HomeView, cerrarSesion
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView,name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/',cerrarSesion,name='salir'),
    
]