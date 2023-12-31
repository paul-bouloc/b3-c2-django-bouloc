from urllib.parse import urlencode
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from app.forms import CustomUserCreationForm
from app.models import Passwords

# Create your views here.


def dashboard(request):
    if request.user.is_authenticated:
        passwords = Passwords.objects.filter(user=request.user)
        # Truncate the website name to make it look better
        for password in passwords:
            password.website = password.website.replace("http://", "").replace("https://", "").replace("www.", "")
            password.website = password.website.split("/")[0]
        return render(request, "app/dashboard.html", {"passwords": passwords})
    else:
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

def detail(request, id):
    # If the user is not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect(reverse("login"))
    
    # Check if the password exists
    try:
        password = Passwords.objects.get(id=id)
    except Passwords.DoesNotExist:
        return redirect(reverse("dashboard"))
    
    # Check if the password belongs to the user
    if password.user != request.user:
        return redirect(reverse("dashboard"))
    
    # Render the detail page
    return render(request, "app/detail.html", {"password": password})

def edit(request, id):
    # If the user is not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect(reverse("login"))
    
    # Check if the password exists
    try:
        password = Passwords.objects.get(id=id)
    except Passwords.DoesNotExist:
        return redirect(reverse("dashboard"))
    
    # Check if the password belongs to the user
    if password.user != request.user:
        return redirect(reverse("dashboard"))
    
    # Render the edit page
    return render(request, "app/edit.html", {"password": password, "id": id})

def editSubmit(request, id):
    # If the user is not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect(reverse("login"))
    
    # Check if the password exists
    try:
        password = Passwords.objects.get(id=id)
    except Passwords.DoesNotExist:
        return redirect(reverse("dashboard"))
    
    # Check if the password belongs to the user
    if password.user != request.user:
        return redirect(reverse("dashboard"))
    
    # Check if the request is a POST request
    if request.method != "POST":
        return redirect(reverse("edit", kwargs={"id": id}))
    
    # Check if all fields are present
    if 'name' not in request.POST or 'website' not in request.POST or 'login' not in request.POST or 'password' not in request.POST:
        baseUrl = reverse("edit", kwargs={"id": id})
        queryString = urlencode({'error': 'Please fill out all fields.'})
        return redirect(f"{baseUrl}?{queryString}")
    
    # Build the data
    post_name = request.POST["name"]
    post_website = request.POST["website"]
    post_login = request.POST["login"]
    post_password = request.POST["password"]
    
    # Check if any fields are empty
    if post_name == "" or post_website == "" or post_login == "" or post_password == "":
        baseUrl = reverse("edit", kwargs={"id": id})
        queryString = urlencode({'error': 'Please fill out all fields.'})
        return redirect(f"{baseUrl}?{queryString}")
    
    # Update the data
    password.name = post_name
    password.website = post_website
    password.login = post_login
    password.password = post_password
    password.save()
    
    # Redirect to the dashboard
    baseUrl = reverse("detail", kwargs={"id": id})
    queryString = urlencode({'success': 'Password edited successfully.'})
    return redirect(f"{baseUrl}?{queryString}")

def delete(request, id):
    # If the user is not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect(reverse("login"))
    
    # Check if the password exists
    try:
        password = Passwords.objects.get(id=id)
    except Passwords.DoesNotExist:
        return redirect(reverse("dashboard"))
    
    # Check if the password belongs to the user
    if password.user != request.user:
        return redirect(reverse("dashboard"))
    
    # Render the delete page
    return render(request, "app/delete.html", {"password": password, "id": id})

def deleteSubmit(request, id):
    # If the user is not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect(reverse("login"))
    
    # Check if the password exists
    try:
        password = Passwords.objects.get(id=id)
    except Passwords.DoesNotExist:
        return redirect(reverse("dashboard"))
    
    # Check if the password belongs to the user
    if password.user != request.user:
        return redirect(reverse("dashboard"))
    
    # Delete the data
    password.delete()
    
    # Redirect to the dashboard
    baseUrl = reverse("dashboard")
    queryString = urlencode({'success': 'Password deleted successfully.'})
    return redirect(f"{baseUrl}?{queryString}")