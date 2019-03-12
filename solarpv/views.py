from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'solarpv/index.html')

def login(request):
    return render(request, 'solarpv/login.html')

def join(request):
    return render(request, 'solarpv/join.html')

def dashboard(request):
    return render(request, 'solarpv/dashboard.html')