from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from .models import USERS, Chat_Room, Chat_Message 
from rest_framework.decorators import api_view 


from rest_framework.response import Response

def login_view(req):
  if req.method == 'POST':
    username= req.POST['username']
    password = req.POST['password']
    user = User.objects.filter(username=username)
    if len(user) == 0:
      return redirect('/login/')
    user = user[0]
    if user.check_password(password):
      req.session['username'] = username  # Store the username in the session
      return redirect('/chat/')
    else:
      return redirect('/login/')
  else:
    # Render the login form
    return render(req, 'LoginPage.html')
  

from django.contrib import messages
def register_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    if User.objects.filter(username=username).exists():
      messages.error(request, 'Username already exists.')
      return redirect('register_view')

    User.objects.create_user(username=username, password=password)
    messages.success(request, 'Account created successfully.')
    return redirect('login_view')

  return render(request, 'LoginPage.html')


def chatPage(request):
  if request.method == "GET":
    chat_rooms = Chat_Room.objects.all()
    username = request.session.get('username', '')  # Get the username from the session
    return render(request, 'chatPage.html', {'chat_rooms': chat_rooms, 'username': username})