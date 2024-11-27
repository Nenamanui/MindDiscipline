from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm


def enter_screen(request):
    template_name = 'homepage/homepage.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage.html')
    else:
        form = SignUpForm()
    return render(request, template_name, {'form': form})

def code_check_screen(request):
    template_name = 'homepage/code_check.html'
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage.html')
    return render(request, template_name, {'form': form})


def profile(request):
    template_name= 'homepage/profile.html'
    return render(request, template_name)


def about(request):
    template_name= 'homepage/about.html'
    return render(request, template_name)