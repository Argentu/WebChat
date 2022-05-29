from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('reg/', views.RegisterUser, name='signup'),
    path('room/', views.index, name='index'),
    path('create/', views.create_chatroom, name='create_chatroom'),
    path('room/<str:room_name>/', views.room, name='room'),
    ]
