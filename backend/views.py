# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from item.models import Category,Item
from .forms import SignUpForm
from django.contrib.auth import logout


def index(request):
    obj = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request,'index.html',{'categories':categories,'unsold':obj})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)        
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

def Logout(request):
    logout(request)
    return redirect('login')  