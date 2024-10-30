from django.urls import path

from . import views

urlpatterns = [
    path('', views.practices),
    path('<int:pk>/', views.practice)
    ]