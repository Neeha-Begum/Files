from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
# Create your views here.

def loginView(request):
    if request.method=="POST":
        a=request.POST.get('user')
        b=request.POST.get('password')
        result=authenticate(request,username=a,password=b)
        print(result)
        if result:
            login(request,result)
            return redirect('homepage')
    return render(request,'login.html')

@login_required(login_url='loginpage')
def homeView(request):
    result=User.objects.all()
    return render(request,'home.html',{'res':result})

@login_required(login_url='loginpage')
def aboutView(request):
    return render(request,'about.html')

@login_required(login_url='loginpage')
def contactView(request):
    return render(request,'contact.html')

@login_required(login_url='loginpage')
def postView(request):
    return render(request,'post.html')

def func1(request):
    if request.method=="POST":
        a=request.POST.get('username')
        if User.objects.filter(username=a).exists():
            obj=User.objects.get(username=a)
            result=obj
        else:
            result=None
        return render(request,'form.html',{'res':result})
    return render(request,'form.html')        