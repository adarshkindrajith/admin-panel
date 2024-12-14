from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.db import IntegrityError
# Create your views here.
def index(request):
    return render(request, 'index.html')

@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('owner')
            else:
                login(request, user)
                return redirect('home')
        else:
            messages.info(request, 'Invalid username or password')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists. Please choose another one.")
            return redirect('signup')
        elif User.objects.filter(email=email):
            messages.error(request, "Email is already registered. Please use a different email.")
            return redirect('signup')
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            return redirect('loginn')
    
    return render(request, 'signup.html')


@login_required(login_url='loginn')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def home(request):
    return render(request, 'home.html')

@login_required(login_url='loginn')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('loginn')


@login_required(login_url='loginn')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def owner(request):
    mem=User.objects.all()
    return render(request,'owner.html',{'mem':mem})

def deleted(request,id):
    mem=User.objects.get(id=id)
    mem.delete()
    return redirect("owner")


@login_required(login_url='loginn')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def updata(request,id):
    mem=User.objects.get(id=id)
    return render(request,'updata.html',{'mem':mem})

def data(request,id):
    x=request.POST['username']
    y=request.POST['email']
    mem=User.objects.get(id=id)
    mem.username=x
    mem.email=y
    mem.save()
    return redirect("owner")
    
@login_required(login_url='loginn')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def addmem(request):
    return render(request, "addmem.html")
def addnew(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists. Please choose another one.")
            return redirect('addmem')
        elif User.objects.filter(email=email):
            messages.error(request, "Email is already registered. Please use a different email.")
            return redirect('addmem')
        try:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            return redirect('owner')
        except IntegrityError:
            messages.error(request, "user exist ")
    return render(request, "addmem.html")    
    

