from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home/')
        else:
            messages.success(request,"ERROR! INVALID CREDENTIALS")
            return redirect('login/')
    else:
        return render(request,'authentication/login.html',{})
    
def signup_user(request):
    if request.method == "POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password1")
        cpassword=request.POST.get("password2")
        my_user=User.objects.create_user(uname,email,password)
        my_user.save()
        return redirect("/")
        print(uname,email,password,cpassword)




    return render(request,'authentication/registration.html')


