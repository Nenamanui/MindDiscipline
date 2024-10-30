from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template_name = 'homepage/homepage.html'
    return render(request, template_name)

def practice(request, pk):
    return HttpResponse('Тренировка номер', pk)