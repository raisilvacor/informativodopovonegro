from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('noticias/', views.noticias_list, name='noticias'),
    path('memoria-viva/', views.memoria_viva, name='memoria_viva'),
    path('territorios/', views.territorios, name='territorios'),
    path('multimidia/', views.multimidia, name='multimidia'),
    path('participe/', views.participe, name='participe'),
]
