from django.urls import path

from . import views

app_name = 'child'

urlpatterns = [
    path('', views.child_info, name='child_info')
    ]