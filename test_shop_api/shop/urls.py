
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'shop_view/', views.shop_view),
    url(r'director_view/', views.director_view),
    url(r'', views.index),
]
