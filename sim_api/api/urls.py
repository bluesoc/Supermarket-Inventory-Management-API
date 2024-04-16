from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/', views.view, name='view'),
    path('view/<int:id>', views.view, name='view'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('search', views.search, name='search'),
]