from django.shortcuts import render
from django.contrib.auth import logout
from .models import Game

# Create your views here.
def display_home(request):
    return render(request, 'landingPage/index.html')

def display_create(request):
    return render(request, 'create/index.html')

def display_dash(request):
    return render(request, 'dashboard/index.html')

def display_test(request):
    return render(request, 'test/index.html')

def games_db(request):
    games_list = Game.objects.all()
    return render(request, 'test/games_db.html', {'Game': games_list})

def display_login(request):
    return render(request, 'accounts/login/login.html')

def logout_view(request):
    return render(request)
