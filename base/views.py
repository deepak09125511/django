from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room
from django.shortcuts import get_object_or_404, render
from .form import RoomForm
# Create your views here.

def the_rooms(request):
    rooms = Room.objects.all()
    return render(request,'the_rooms.html',{'rooms':rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'room_detail.html', {'room': room})

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,"room_form.html",context)

def update_room(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form':form}
    return render(request,'room_form.html',context)

def delete_room(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request,'delete.html',{'obj': room})
         
