from django.contrib.auth import logout
from django.shortcuts import redirect, render

def index(request):
    if request.user.is_authenticated:
        return redirect("home:index")
    else:
        return redirect("auth:login")

def login(request):
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("auth:login")
