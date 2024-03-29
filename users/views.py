from django.contrib.auth import get_user_model, login, authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LoginForm, RegisterUserForm, AuthenticationForm


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('news_list'))
            else:
                form.add_error(None, "Неправильные данные")
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('news_list')


def register_page(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            login(request, user)
            return redirect('news_list')
        else:
            form.add_error(None, "Неправильные данные.")
    return render(request, 'users/register.html', {'form': RegisterUserForm()})

