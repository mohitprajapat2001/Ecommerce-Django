from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('userlogin', views.userlogin, name='userlogin'),
    path('register', views.register, name='register'),
    path('User/<str:u>', views.userdetails, name='account Details'),
    path('edituser', views.edituser, name=" edituser"),
    path('logout', views.logout, name=" logout"),
]
