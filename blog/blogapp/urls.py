from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('like/<int:post_id>/', views.like, name='like'),
]
