from django.urls import path

from . import views

app_name = 'coach'

urlpatterns = [
    path('', views.coach_info, name='coach_info')
    ]