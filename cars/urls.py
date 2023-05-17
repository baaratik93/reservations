from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarHomePage),
    path('new/', views.NewCarSubmit,name='NewCarSubmit'),
    # path('new/', views.NewCarSubmit,name="nouveau"),
]
