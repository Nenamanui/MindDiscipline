from django.shortcuts import render
from django.http import HttpResponse

def event_info(request):    
    return HttpResponse('event')