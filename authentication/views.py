from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomAuthenticationForm, CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"User {user.username} created successfully!")
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('event_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/authentication/login')


