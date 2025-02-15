from django.urls import path
from .views import the_rooms
from .views import room_detail
from .views import create_room
from .views import update_room
from .views import delete_room


  

urlpatterns = [
    path('', the_rooms, name='home'),
    path('rooms/',the_rooms,name='the_rooms'),
    path('room/<int:room_id>',room_detail,name='room-detail'),
    path('create-room/',create_room,name = 'create-room'),
    path('update-room/<str:pk>',update_room,name = 'update-room'),
    path('delete-room/<int:pk>',delete_room,name = 'delete-room'),
]