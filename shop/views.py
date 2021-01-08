from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as log

# Create your views here.
def index(request):
   return HttpResponse('this is home page')

def login(request):
    if request.user.is_authenticated:
        return redirect('/game')
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate (request, username=username, password=password)
        print(user)
        if user is not None:
            log(request,user)
            return redirect('/game')
        else:
            return HttpResponse("<h1>User not found</h1>")  
    else:
        return render(request,'login.html')

def logout_view(request):
    logout(request)
    print('logout')
    return redirect('/')
 
def game(request):
    return render(request, 'gamemanu.html') 

@login_required(login_url='')
def firstg(request):
    return render(request,'2048.html')      

def reg(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account created for '+user)
            return redirect('/')
        else:
            print(form.errors.as_data)

            return HttpResponse('happp')
    
    return render(request,'reg.html',{'form':form})