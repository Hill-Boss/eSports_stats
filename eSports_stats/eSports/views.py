from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from .models import User, Role, Staff, Status, Player, Game, Team_Rank, Team, user_team, Stats, user_game

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
    return render(request, 'viewData/index.html')

def display_login(request):
    return render(request, 'accounts/login/login.html')

def logout_view(request):
    return render(request)

@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        pass

@csrf_exempt
def ajax_getStats(request):
    if request.method == 'GET':
        pass

@csrf_exempt
def ajax_getGamePlayer(request):
    if request.method == 'GET':
        return JsonResponse(User_Game(), safe=False)

@csrf_exempt
def ajax_CreateUser(request):
    if request.method == 'POST':
        U = User(login_name=request.data.username, first_name=request.data.first_name, last_name=request.data.last_name, email=request.data.email, discord=request.data.discord)
        U.save()
        print(U.id)
        # return HttpResponse(U, safe=False)


def User_Game():
    user_game_list = user_game.objects.all()
    games_list = Game.objects.all()
    response = {}
    for game in games_list:
        obj = []
        for player in user_game_list:
            if player.game_id.name == game.name:
                obj.append(player.username)

        response[game.name] = obj
    return response
