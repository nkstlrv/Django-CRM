from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from crm.forms import RegisterForm
from .models import Record


def index(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "You have logged in")
            return redirect('home')
        else:
            messages.success(request, "Wrong credentials. Please try again")

    return render(request, 'crm/index.html', {'records': records})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been successfully registered")

            return redirect('home')
    else:
        form = RegisterForm()
        return render(request, 'crm/register.html', {'form': form})
    return render(request, 'crm/register.html', {'form': form})
