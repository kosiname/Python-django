from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password doesn\'t match')
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('KosinameChat')
        else:
            messages.info(request, 'Incorrect credentials')
            return redirect('login')   
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('login')

def KosinameChat(request):
    return render(request, 'KosinameChat.html')

def checkview(request):
    if request.method == 'POST':
        user = request.POST['username']
        global chatroom
        chatroom = request.POST['roomname']
        check_user = auth.authenticate(username=user)
        if User.objects.filter(username=user).exists():
            if Room.objects.filter(roomname=chatroom).exists():
                return redirect('/'+chatroom+'/?username='+user)
            else:
                new_room = Room.objects.create(roomname=chatroom)
                new_room.save()
                return redirect('/'+chatroom+'/?username='+user)
        else:
            messages.info(request, 'Username does\'t exist. Register and Try again')
            return redirect('KosinameChat')
    else:
        return render(request, 'KosinameChat.html')
    
def chatroom(request, chatroom):
    username = request.GET.get('username')
    room_details = Room.objects.get(roomname=chatroom) 
    context = {
        'username' : username,
        'room' : chatroom,
        'room_details' : room_details
    }
    return render(request, 'chatroom.html', context)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse("Message sent successfully")

def getMessages(request, chatroom):
    room_details = Room.objects.get(roomname=chatroom)
    messages = Message.objects.filter(room=room_details.id)
    context1 = {
        'messages' : list(messages.values())
    }
    return JsonResponse(context1)

