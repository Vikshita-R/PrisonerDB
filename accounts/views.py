from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == "POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]
        username = request.POST["name"]
    
        if not User.objects.filter(username=username).exists() and not User.objects.filter(email=email).exists():
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            data = {
                'name' : first_name + " " + last_name,
                'username' : username,
                'email' : email
            }
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return render(request, "accounts/registered.html", data)

        elif User.objects.filter(username=username).exists():
            data = {
                "error" : "Username already exists, Choose another username"
            }
            return render(request, "accounts/register.html", data)
        
        elif User.objects.filter(email = email).exists():
            data = {
                "error" : "Email already exists"
            }
            return render(request, "accounts/register.html", data)

    else:
        return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            data={
                'error': "Invalid Credentials. Please register."
            }
            return render(request, "accounts/login.html", data)
    else:
        return render(request, "accounts/login.html")
    
def logout(request):
    auth.logout(request)
    return redirect("/")