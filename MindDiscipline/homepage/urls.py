from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.WelcomeScreenView.as_view(), name='welcomescreen'),
    path('login/', views.PhoneAuthView.as_view(), name='phoneauth'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    # path('confirm/', views.code_check_screen, name='code_check_screen'),
    # path('about/', views.about, name='about'),

] 