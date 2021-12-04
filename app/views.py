from django import http
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import re
from app.models import *
from app.models import User
import bcrypt

def logout(request):
    request.session.clear()
    return redirect('/')

def register(request):
    Name = request.POST['name']
    Username = request.POST['username']
    Password = request.POST['password']
    new_user = User.objects.create(name = Name, username=Username,password=Password)
    print(new_user)
    request.session['user_id']=new_user.id
    return redirect('/')

def main(request):
    return render(request,'main.html')

def dashboard(request):
    return render(request,'dashboard.html')

def wish_items(request):
    return render(request,'wish_items.html')

def wish_items_create(request):
    return render(request,'wish_items_create.html')