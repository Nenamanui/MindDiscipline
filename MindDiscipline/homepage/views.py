from django.shortcuts import render


def enter_screen(request):
    template_name = 'homepage/homepage.html'
    return render(request, template_name)

def code_check_screen(request):
    template_name = 'homepage/code_check.html'
    return render(request, template_name)