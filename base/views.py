from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Room,Topic
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .form import RoomForm
# Create your views here.

def login_page(request):
    # taking data from the user
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')


    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect('login') 
        
        # authentication of the user
        authenticated_user = authenticate(request,username = username,password = password)
        
        # making login the user
        if authenticated_user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"The user does not exist")

    context ={'page':page}
    return render(request,'login_register.html',context)

def logout_user(request):
    logout(request)
    return render(request,"the_rooms.html")

def register_page(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        messages.error("An error occured during registration")
        
    return render(request,'login_register.html',{'form':form})

def the_rooms(request):
    q = request.GET.get('q') if request.GET.get('q') !=None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q)|
                                Q(name__icontains=q)|
                                Q(description__icontains=q)).order_by('-created')
    topics = Topic.objects.all()
    room_count = rooms.count()
    context ={'rooms':rooms,'topics':topics,'room_count':room_count,'search_query': q}
    return render(request,'the_rooms.html',context)

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'room_detail.html', {'room': room})

@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,"room_form.html",context)

@login_required(login_url='login')
def update_room(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("You are not allowed here")

    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form':form}
    return render(request,'room_form.html',context)

@login_required(login_url='login')
def delete_room(request,pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("You are not allowed here")
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request,'delete.html',{'obj': room})
         
