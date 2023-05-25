from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.LoginUser,name='LoginUser'),
    path('signin/', views.SigninUser,name='SigninUser'),
    path('deconnexion/', views.Disconnect,name='Disconnect'),
]
