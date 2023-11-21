from django.urls import path
from . import views


urlpatterns = [
    path('room/', views.chat_room, name='room'),
]