
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('blogpost/<int:id>/', views.blogpost,name="blogPost"),
]
