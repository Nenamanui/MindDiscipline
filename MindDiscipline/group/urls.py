from django.urls import path

from . import views

app_name = 'group'

urlpatterns = [
    path('<int:pk>/', views.group_info, name='group_info')
    ]