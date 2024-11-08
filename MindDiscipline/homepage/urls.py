from django.urls import path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.enter_screen, name='enter_screen'),
    path('about/', views.about, name='about')
] 