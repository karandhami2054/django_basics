from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),

]