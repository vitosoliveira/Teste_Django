from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, "help.html")

def forget_password (request):
    return  render(request, "forgot-password.html")

def register (request):
    return render(request, "register.html")

def erro_404(request):
    return  render (request, "404.html")

def index(request):
    return  render(request, "index.html")

def login(request):
    return  render(request, "login.html")