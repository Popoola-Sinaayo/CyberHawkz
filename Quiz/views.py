from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Quiz_User

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username, password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        return render(request, 'index.hrml', {'message': 'Invalid Credentials'})
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'home.html')
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        email = request.data["email"]
        user = Quiz_User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        login(request, user)
        return render(request, 'home.html')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'home.html')
        return render(request, 'index.html')


def board(request):
    users_in_rank = Quiz_User.objects.all().order_by('-score')
    return render(request, 'rank.html', {'user': users_in_rank})
