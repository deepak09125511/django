from django.urls import path
from .views import the_rooms
from .views import room_detail
from .views import create_room
from .views import update_room
from .views import delete_room
from .views import login_page
from .views import logout_user
from  .views import register_page


  

urlpatterns = [
    path('login/',login_page,name = "login"),
    path('register/',register_page,name = "register"),
    path('logout/',logout_user,name = "logout"),
    path('', the_rooms, name='home'),
    path('rooms/',the_rooms,name='the_rooms'),
    path('room/<int:room_id>',room_detail,name='room-detail'),
    path('create-room/',create_room,name = 'create-room'),
    path('update-room/<str:pk>',update_room,name = 'update-room'),
    path('delete-room/<int:pk>',delete_room,name = 'delete-room'),
]