from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from .models import User
from .forms import SignUpForm, PhoneForm, LoginForm, RegisterForm
from django.views.generic import TemplateView, FormView

user = get_user_model()

class WelcomeScreenView(TemplateView):
    template_name = 'homepage/homepage.html'
    model = user


class PhoneAuthView(FormView):
    template_name = 'homepage/auth.html'
    model = user
    form_class = PhoneForm

    def form_valid(self, form):
        phone = form.cleaned_data['phone']
        self.request.session['phone'] = phone
        try:
            User.objects.get(phone_number=phone)
            return redirect(LoginView) #???
        except User.DoesNotExist:
            self.request.form_class = RegisterForm
            
            user = User.objects.create_user(
                phone_number=phone,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(self.request, user)
            return redirect('profile')


class LoginView(FormView):
    template_name = 'homepage/auth.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if not request.session.get('phone'):
            return redirect('phone_input')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        phone = self.request.session.get('phone')
        user = authenticate(self.request, phone=phone, password=form.cleaned_data['password'])
        if user:
            login(self.request, user)
            return redirect('profile')
        else:
            form.add_error(None, "Неверный пароль")
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone'] = self.request.session.get('phone')
        return context


class RegisterView(FormView):
    template_name = 'homepage/auth.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        if not request.session.get('phone'):
            return redirect('phone_input')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        phone = self.request.session.get('phone')
        user = User.objects.create_user(
            phone=phone,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return redirect('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone'] = self.request.session.get('phone')
        return context


class AboutView(TemplateView):
    template_name = 'homepage/about.html'


class ProfileView(TemplateView):
    template_name= 'homepage/profile.html'

