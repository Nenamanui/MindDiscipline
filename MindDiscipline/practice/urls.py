from django.urls import path

from . import views

app_name = 'practice'

urlpatterns = [
    path('', views.practices_list, name='practices_list'),
    path('<int:pk>/', views.practice_info, name='practice_info')
    ]