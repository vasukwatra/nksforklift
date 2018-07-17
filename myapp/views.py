from django.shortcuts import render
from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponseRedirect
from .forms import NKS_form
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')


def courses(request):
    return render(request, 'courses.html')


def safetyrules(request):
    return render(request, 'safetyrules.html')


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')


def findus(request):
    return render(request,'findus.html')


def Schedule(request):
    return render(request, 'Schedule.html')



def register(request):
    if request.method=='POST':
        form=NKS_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Register Successfully")
            return HttpResponseRedirect('/myapp/register/')
        else:
            messages.error(request,"invalid form")
    else:
         form=NKS_form()

    return render(request,'form.html',{"form":form})


def login(request):

    if request.method == 'POST':
        user_name=request.POST['user']
        passw=request.POST['password']
        try:
            user=auth.authenticate(username=user_name,password=passw)
            if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect('/myapp/register/')
            else:
                messages.error(request,"Invalid password")
        except auth.ObjectNotExist:
            messages.error(request,"Invalid User")

    return render(request,'login.html')


def m1(request):
    return render(request, '1machine.html')

def m2(request):
    return render(request, '2machine.html')

def m3(request):
    return render(request, '3machine.html')

def m4(request):
    return render(request, '4machine.html')

def m5(request):
    return render(request, '5machine.html')

def gallery(request):
    return render(request, 'gallery.html')
