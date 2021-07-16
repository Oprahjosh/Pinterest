from django.contrib.auth import logout , login
from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.http import request


# Create your views here.

def index(request):
    return render(request, 'accounts/index.html', )

def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('/dashboard')
    else:
        form = RegisterForm
    return render ( response , 'accounts/signup.html' , {'form': form} )

def dashboard(request):
    return render(request, 'accounts/dashboard.html', )

def logout_request(request):
    logout(request)

    return redirect("accounts/index.html")

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
        return redirect('/dashboard')
    else:
        form = LoginForm()
    return render(request = request,
                    template_name = "accounts/login.html",
                    context={"form":form})