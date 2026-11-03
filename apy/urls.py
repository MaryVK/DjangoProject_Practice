from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/biography/', views.biography, name='biography'),
    path('about/facts/', views.facts, name='facts'),
    path('city/info/', views.city_info, name='city_info'),
    path('city/places/', views.city_places, name='city_places'),
]