from django.shortcuts import render
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .models import Role
from .models import Staff
from .models import Status
from .models import Player
from .models import Game
from .models import Team_Rank
from .models import Team
from .models import user_team
from .models import Stats
from .models import user_game

# Create your views here.
def display_home(request):
    return render(request, 'landingPage/index.html')

def display_create(request):
    return render(request, 'create/index.html')

def display_dash(request):
    return render(request, 'dashboard/index.html')

def display_test(request):
    user_list = User.objects.all()
    staff_list = Staff.objects.all()
    player_list = Player.objects.all()
    games_list = Game.objects.all()
    Team_list = Team.objects.all()
    user_team_list = user_team.objects.all()
    user_game_list = user_game.objects.all()
    return render(request, 'test/index.html', {
        'Users': user_list,
        'Staff': staff_list,
        'Players': player_list,
        'Games': games_list,
        'Teams': Team_list,
        'user_team': user_team_list,
        'user_game': user_game_list
        })

def db_data(request):
    user_list = User.objects.all()
    staff_list = Staff.objects.all()
    player_list = Player.objects.all()
    games_list = Game.objects.all()
    Team_list = Team.objects.all()
    user_team_list = user_team.objects.all()
    user_game_list = user_game.objects.all()
    return render(request, 'test/db_data.html', {
        'Users': user_list,
        'Staff': staff_list,
        'Players': player_list,
        'Games': games_list,
        'Teams': Team_list,
        'user_team': user_team_list,
        'user_game': user_game_list
        })

def display_data(request):
    user_game_list = user_game.objects.all()
    return render(request, 'viewData/index.html', {'user_game': user_game_list})

def display_login(request):
    return render(request, 'accounts/login/login.html')

def logout_view(request):
    return render(request)

@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        pass
