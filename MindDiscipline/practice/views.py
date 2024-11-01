from django.shortcuts import render

def practices(request):    
    template_name = 'practice/practices.html'
    gjopa = 'JOPAA'
    context = {
        'jopa': gjopa,
    }
    return render(request, template_name, context)

def practice(request, pk):
    template_name = 'practice/practice.html'
    pk = pk
    context = {
        'pk': pk,
    }
    return render(request, template_name, context)