from phonenumber_field.modelfields import PhoneNumberField
from homepage.models import User
from django import forms

class SignUpForm(forms.Form):
    phone = PhoneNumberField()
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password')


class PhoneForm(forms.Form):
    phone = forms.CharField(label='Номер телефона', max_length=18)

class LoginForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)