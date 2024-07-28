from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('avis/', views.avis, name='avis'),
    path('menus/', views.menus, name='menus'),
    path('reservation/', views.reservation, name='reservation'),
]