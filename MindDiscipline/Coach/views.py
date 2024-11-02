from django.shortcuts import render
from django.http import HttpResponse

def coach_info(request):    
    return HttpResponse('коачи') 