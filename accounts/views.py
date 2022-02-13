import django
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as l
# Create your views here.
def userregister(request):
    form=UserRegisterForm()
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('register')
        else :
             context={
            'form':form
        }
        return render(request,'accounts/register.html',context)
    else :
        context={
            'form':form
        }
        return render(request,'accounts/register.html',context)


def userlogin(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            print(user)
            if user is not None:
                l(request,user)
                return HttpResponse('login')
        
        else:
            print(form.errors)
            context={
                'form':form
                
            }
            return render(request,'accounts/login.html',context)
    else:
        context={
            'form':form
        }
        return render(request,'accounts/login.html',context)




