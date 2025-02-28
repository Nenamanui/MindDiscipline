# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from phonenumber_field.modelfields import PhoneNumberField
from homepage.models import User
from django import forms

class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Необязательно')
    phone = PhoneNumberField()

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(label='Имя пользователя')
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name']  # Дополнительные поля

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']