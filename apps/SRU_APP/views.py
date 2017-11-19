from __future__ import unicode_literals
from .models import User
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect

def index(request):
  context = {
    'users': User.objects.all()
  }
  return render(request,'index.html', context)

def new(request):
  return render(request,'newuser.html')

def edit(request, user_id):
  # need to grabe the correct user id to identify the user
  context = {
      'user': User.objects.get(id=user_id)
  }
  return render(request,'edituser.html', context)
  
def create(request):
  result = User.objects.validate(request.POST)
  if type(result) == list:
    for err in result:
      messages.error(request, err)
    return redirect('/users/new')
  return redirect('/users')

def update(request,user_id):
  # result = User.objects.validate(request.POST)
  # if type(result) == list:
  #   for err in result:
  #     messages.error(request, err)
  #   return redirect('/users/{}/edit'.format(user_id))

  updated_user = User.objects.get(id=user_id)
  updated_user.fname=request.POST['fname']
  updated_user.lname=request.POST['lname']
  updated_user.email=request.POST['email']
  updated_user.save()
  # pulling the data and updating it
  return redirect('/users')

def show(request, user_id):
  context = {
    'user': User.objects.get(id=user_id)
  }
  print context['user']
  return render(request, 'show.html',context)

def destroy(request, user_id):
  User.objects.get(id=user_id).delete()
  return redirect('/users')


