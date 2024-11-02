from django.shortcuts import render

def group_info(request, pk):    
    template_name = 'group/group.html'
    # нулевая в строке поиска ???
    groups = [{'name': 'gryppa 1', 'desc': 'pervaya'}, 
            {'name': 'gryppa 2', 'desc': 'vtoraya'}]
    context = {
        'group': groups[pk],
    }
    return render(request, template_name, context)