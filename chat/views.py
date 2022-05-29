import os.path
from datetime import datetime
from hashlib import sha1
from django.shortcuts import render, redirect
from chat.forms import RegisterUserForm
from django.contrib.auth import login as log_dj, authenticate
from test_task.settings import BASE_DIR
from .models import *
from django.contrib.sites.shortcuts import get_current_site
from random import randint
import json


def RegisterUser(request):
    user_creation_form = RegisterUserForm(request.POST or None)
    if request.method == 'POST' and user_creation_form.is_valid():
        u_name = user_creation_form.cleaned_data.get('username')
        u_pass = user_creation_form.cleaned_data.get('password2')
        user_creation_form.save()
        user = authenticate(username=u_name,
                            password=u_pass)
        log_dj(request, user)
        return redirect(login)
    return render(request, 'chat/reg.html', {'form': user_creation_form})


def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST' and len(request.POST) == 2:
            model = MyUser.objects.all()
            user_names = [i.username for i in model]
            inp = request.POST['usrnm']
            if inp in user_names:
                return render(request, 'chat/user.html', {'exist': True, 'name': inp})
            else:
                return redirect(RegisterUser)
        elif request.method == 'POST' and len(request.POST) == 3:
            user = authenticate(username=request.POST['usrnm'],
                                password=request.POST['passwd'])
            log_dj(request, user)
            return redirect(login)
        else:
            return render(request, 'chat/user.html')
    else:
        return redirect(index)


def index(request):
    if not request.user.is_authenticated:
        return redirect(login)
    else:
        chats = Chatroom
        chats = chats.objects.filter(Users__username=request.user.username)
        chats = [i.name for i in chats]
        return render(request, 'chat/index.html', {'chats': chats})


def room(request, room_name):
    if not request.user.is_authenticated:
        return redirect(login)
    else:


        return render(request, 'chat/room.html', {
            'room_name': room_name,
            'username': request.user.username,
            'usr_color': f'rgb({randint(30, 230)}, {randint(30, 230)}, {randint(30, 230)})'
        })


def create_chatroom(request):
    if not request.user.is_authenticated:
        return redirect(login)
    elif request.method == 'POST':
        name = request.POST['chtnm']
        hashed_name = sha1(name.encode() + str(datetime.now().time()).encode()).hexdigest()
        logs = os.path.join(BASE_DIR, 'media', 'logs')
        file = os.path.join(logs, hashed_name + '.json')
        log = open(file, 'w+')
        log.close()

        link = f'{hashed_name}'
        log = hashed_name+'.json'
        chatroom = Chatroom(name=name, invite_link=link, Log_file=log)
        chatroom.save()
        usr = MyUser.objects.filter(username=request.user.username)[0]
        chatroom.Users.add(usr)
        return redirect(index)
    else:
        return render(request, 'chat/create.html')

# {'url': f'http://{get_current_site(request).domain}/{request.user.username}/invite/'})
