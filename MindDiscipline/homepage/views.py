from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model#, authenticate
from .forms import SignUpForm #, LoginForm
from django.views.generic import TemplateView

User = get_user_model()


def phone_auth_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            try:
                user = User.objects.get(phone=phone)
                # Если пользователь найден - переход на страницу ввода пароля
                return redirect('', phone=phone)
            except User.DoesNotExist:
                # Если пользователя нет - переход на регистрацию
                request.session['registration_phone'] = str(phone)
                return redirect('register')
    else:
        form = SignUpForm()
    return render(request, 'auth/phone_input.html', {'form': form})

def login_with_password(request, phone):
    # (используйте django.contrib.auth.views.LoginView)
    ...

def registration_view(request):
    pass
    # if request.method == 'POST':
    #     form = # RegistrationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.phone = request.session.get('registration_phone')
    #         user.save()
    #         login(request, user)
    #         return redirect('profile')
    # else:
    #     form = #RegistrationForm()
    # return render(request, 'auth/register.html', {'form': form})



class WelcomeScreenView(TemplateView):
    template_name = 'homepage/homepage.html'
    model = User


# def welcome_screen(request):
#     template_name = 'homepage/homepage.html'
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('profile.html')
#     else:
#         form = SignUpForm()
#     return render(request, template_name, {'form': form})

# def code_check_screen(request):
#     template_name = 'homepage/code_check.html'
#     form = LoginForm(data=request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('homepage.html')
#     return render(request, template_name, {'form': form})


# def profile(request):
#     template_name= 'homepage/profile.html'
#     return render(request, template_name)


# def about(request):
#     template_name= 'homepage/about.html'
#     return render(request, template_name)