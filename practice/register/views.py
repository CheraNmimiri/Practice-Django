from django.shortcuts import render

from .models import User
# Create your views here.


def register(request):
    return render(request, 'register.html')


def validate(request):
    if request.method == "POST":
        user = User()
        user.name = request.POST.get("name")
        user.username = request.POST.get("username")
        user.password = request.POST.get("password")
        user.email = request.POST.get("email")
        user.save()
        context = {
            "name": user.name,
            "username": user.username,
            "password": user.password,
            "email": user.email,
        }  
    return render(request, "validate.html", context)


def login(request):
    return render(request, "login.html")

def check(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        context = {
            "username": username,
            "password": password
        }
        if User.objects.filter(username=username, password=password):
            return render(request, "successfull.html", context)