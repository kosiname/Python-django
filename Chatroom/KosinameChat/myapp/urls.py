from django.urls import path
from myapp import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('KosinameChat', views.KosinameChat, name='KosinameChat'),
    path('<str:chatroom>/', views.chatroom, name='chatroom'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:chatroom>/', views.getMessages, name='getMessages')
]