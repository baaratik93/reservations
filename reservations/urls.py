"""reservations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
    path('reserver/', views.AddReservation),
    path('payement/', views.Payement,name='payement'),
    path('cars/', include('cars.urls')),
    path('connexion/', include('connexion.urls')),
]
# Cette ligne permet d'utiliser les images à partir du dossier media et de localhost
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns = [path('__debug__/', include('debug_toolbar.urls')),] + urlpatterns
    urlpatterns += static(settings.TE_URL, document_root=settings.TE_ROOT)
