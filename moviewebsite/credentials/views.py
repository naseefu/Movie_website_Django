from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username already exist")
            return redirect('credentials:register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email already Taken")
            return redirect('credentials:register')
        else:
            user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)

            user.save();
            print("user created")
        return redirect('credentials:login')

    return render(request, "register.html")

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('movieapp:home')
        else:
            messages.info(request,"Incorrect Username or Password")
            return redirect('credentials:login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('movieapp:home')
