from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import registerUser, Chat_Room, Chat_Message

def chatPage(request):
  if request.method == "GET":
    chat_rooms = Chat_Room.objects.all()
    return render(request, 'chats/chatPage.html', {'chat_rooms': chat_rooms})

def loginUser(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('chat-page')
    else:
      return render(request, 'chats/LoginPage.html', {'error': 'Invalid username or password'})
  else:
    return render(request, 'chats/LoginPage.html')

def logoutUser(request):
  logout(request)
  return redirect('login-user')