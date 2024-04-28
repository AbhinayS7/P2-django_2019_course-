
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('product_page/', views.product_page),
]
