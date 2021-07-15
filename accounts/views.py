from msilib.schema import ListView
from pyexpat.errors import messages
from django.contrib.auth import logout , authenticate , login
from django.shortcuts import render,redirect
from .forms import RegisterForm,AuthenticationForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'accounts/index.html', )

def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/dashboard')
    else:
        form = RegisterForm
    return render ( response , 'accounts/signup.html' , {'form': form} )

def dashboard(request):
    return render(request, 'accounts/dashboard.html', )

def logout_request(request):
    logout(request)

    return redirect("accounts/base.html")

'''def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "registration/login.html",
                  context={"form":form})'''

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "registration/login.html",
                    context={"form":form})