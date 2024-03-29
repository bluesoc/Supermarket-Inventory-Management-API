from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/', views.view, name='view'),
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name='delete'),
]