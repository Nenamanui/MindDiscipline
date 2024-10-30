from django.shortcuts import render
from django.http import HttpResponse

def practices(request):    
    return HttpResponse('practices')

def practice(request, pk):
    return HttpResponse('Тренировка номер', pk)