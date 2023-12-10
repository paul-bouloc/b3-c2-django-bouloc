from urllib.parse import urlencode
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from app.forms import CustomUserCreationForm
from app.models import Passwords

# Create your views here.


def dashboard(request):
    return render(request, "app/dashboard.html")
  
def register(request):
    if request.user.is_authenticated:
        return redirect(reverse("dashboard"))
    
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        
def add(request):
    # If the user is not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect(reverse("login"))
    
    # Otherwise, render the add page
    return render(request, "app/add.html")

def addSubmit(request):
    # If the user is not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect(reverse("login"))
    
    # Check if the request is a POST request
    if request.method != "POST":
        return redirect(reverse("add"))
    
    # Check if all fields are present
    if 'name' not in request.POST or 'website' not in request.POST or 'login' not in request.POST or 'password' not in request.POST:
        baseUrl = reverse("add")
        queryString = urlencode({'error': 'Please fill out all fields.'})
        return redirect(f"{baseUrl}?{queryString}")
    
    # Build the data
    user = request.user
    name = request.POST["name"]
    website = request.POST["website"]
    login = request.POST["login"]
    password = request.POST["password"]
    
    # Check if any fields are empty
    if name == "" or website == "" or login == "" or password == "":
        baseUrl = reverse("add")
        queryString = urlencode({'error': 'Please fill out all fields.'})
        return redirect(f"{baseUrl}?{queryString}")
    
    data = Passwords(user=user, name=name, website=website, login=login, password=password)
    data.save()
    baseUrl = reverse("dashboard")
    queryString = urlencode({'success': 'Password added successfully.'})
    return redirect(f"{baseUrl}?{queryString}")