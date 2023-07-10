from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Products/<int:prod>', views.prodview, name='Product View'),
    path('Products/<str:category>', views.categoryview, name='Category View'),
    path('searchproduct', views.searchproduct, name='Search Product'),

]
