from django.urls import path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.enter_screen, name='enter_screen'),
    path('confirm/', views.code_check_screen, name='code_check_screen'),
    path('about/', views.about, name='about'),
    path('accounts/profile/', views.profile, name='profile')
] 