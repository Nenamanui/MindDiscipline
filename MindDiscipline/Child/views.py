from django.shortcuts import render
from django.http import HttpResponse

def child_info(request):    
    return HttpResponse('childs')
