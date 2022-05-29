from django.shortcuts import render, redirect
from chat.forms import RegisterUserForm
from django.contrib.auth import login as log_dj, authenticate
from .models import MyUser
from django.contrib.sites.shortcuts import get_current_site
from random import randint


def RegisterUser(request):
    user_creation_form = RegisterUserForm(request.POST or None)
    if request.method == 'POST' and user_creation_form.is_valid():
        u_name = user_creation_form.cleaned_data.get('username')
        u_pass = user_creation_form.cleaned_data.get('password2')
        user_creation_form.save()
        #user = authenticate(username=u_name,
        #                    password=u_pass)
        #log_dj(request, user)
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
        return render(request, 'chat/index.html')


def room(request, room_name):
    if not request.user.is_authenticated:
        return redirect(login)
    else:
        return render(request, 'chat/room.html', {
            'room_name': room_name,
            'username': request.user.username,
            'usr_color': f'rgb({randint(28, 230)}, {randint(28, 230)}, {randint(28, 230)})'
        })


def create_chatroom(request):
    if not request.user.is_authenticated:
        return redirect(login)
    else:
        return render(request, 'chat/create.html',
                      {'url': f'http://{get_current_site(request).domain}/{request.user.username}/invite/'})
