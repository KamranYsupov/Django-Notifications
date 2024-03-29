from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', max_length=20)
    password = forms.CharField(
        label='Пароль', min_length=6, max_length=20, widget=forms.PasswordInput()
    )



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', max_length=20)
    password1 = forms.CharField(
        label='Пароль', min_length=6, max_length=20, widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Повтор пароля', min_length=6, max_length=20, widget=forms.PasswordInput()
    )
    class Meta:
        model = get_user_model()
        fields = 'username', 'email', 'first_name', 'last_name', 'password1', 'password2'

