from django.shortcuts import render
from django.http import HttpResponse

def index(request):    
    return HttpResponse('Главная страница') 

def practice(request, pk):
    return HttpResponse('Тренировка номер', pk)