from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarHomePage),
    path('new/', views.NewCarSubmit,name='NewCarSubmit'),
    path('<int:id>/', views.SingleCar,name='SingleCar'),
    path('<int:id>/delete', views.DeleteCar,name='SingleCar'),
]
