from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import JsonResponse
from .models import Chat

import openai
from django.utils import timezone


openai_api_key = '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'
openai.api_key = openai_api_key

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        email = request.POST.get('email', False)
        password1 = request.POST.get('password1', False)
        password2 = request.POST.get('password2', False)
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save();
                return render(request, 'login.html')
        else:
            messages.info(request, 'Password doesn\'t match')
            return redirect('register')
    else:      
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            messages.info(request, 'Incorrect credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('login')

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
            ]
    )
    answer = response.choices[0].message.content.strip()
    return answer

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        chat = Chat.objects.create(user=request.user, message=message, response=response, created_at = timezone.now())
        chat.save()
        context = {
            'message' : message,
            'response' : response
        }
        return JsonResponse(context)
    chats = Chat.objects.filter(user=request.user)
    return render(request, 'chatbot.html', {'chats' : chats})

