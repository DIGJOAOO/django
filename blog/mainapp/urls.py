from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jdc/', views.jdc, name='jdc'),
    path('mapi/', views.mapi, name='mapi'),
    path('pkmn/', views.pkmn, name='pkmn'),
]