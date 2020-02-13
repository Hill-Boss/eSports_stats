from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import User as esp_user
from .models import Role, Staff, Status, Player, Game, Team_Rank, Team, user_team, Stats, user_game

# Create your views here.

# This is to display a message to the user
active_messages = {'viewData': '', 'index': '', 'register': '' }

def redirect_home(request):
    return redirect('/home/')

def display_home(request):
    if active_messages['index'] != '':
        messages.info(request, active_messages['index'])
        active_messages['index'] = ''
    return render(request, 'general/index.html')

def display_register(request):
    if active_messages['register'] != '':
        messages.info(request, active_messages['register'])
        active_messages['register'] = ''
    return render(request, 'general/register.html')


def display_create(request):
    return render(request, 'admin/manageUsers.html')

def display_dash(request):
    return render(request, 'dashboard/index.html')

def display_test(request):
    return render(request, 'test/index.html')

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
    return render(request, 'accounts/User/viewData.html')

# diplay functions above

# ajax calls below

@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        pass



@csrf_exempt
def ajax_loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        active_messages['index'] = 'You have successfully logged in'
        return redirect_home(request)
    else:
        active_messages['index'] = 'Your account was not found or Your password was incorrect'
        return redirect_home(request)

@csrf_exempt
def ajax_logoutUser(request):
    logout(request)
    return redirect_home(request)

@csrf_exempt
def ajax_registerUser(request):
    # try authenticating the user
    user = authenticate(request=None, username=request.POST['email'], password=request.POST['password'])

    # if None then user DNE
    try:
        if user is None:
            first = request.POST['firstname']
            last = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            discord = request.POST['discord']
            print(first, ' ', last, ' ', email, ' ', password, ' ', discord)
            # create django user
            user_acc = User.objects.create_user(email, email, password, first_name=first, last_name=last)
            user_acc.save()

            user = authenticate(request, username=email, password=password)
            # create esp user
            u = esp_user(user_id=user_acc, discord=discord)
            u.save()
            print(u.user_id)

            # login new user
            if user is not None:
                login(request, user)
                active_messages['index'] = 'You have successfully logged in'
                return redirect('/home/')
            else:
                active_messages['register'] = 'Your account was not created for some reason'
                return redirect('/register/')
        else:
            active_messages['register'] = 'That email is already used.'
            return redirect('/register/')
    except Exception as e:
        if str(e) == 'UNIQUE constraint failed: auth_user.username':
            active_messages['register'] = 'That username is already used.'
        else:
            active_messages['register'] = e
        return redirect('/register/')

@csrf_exempt
def ajax_getGamePlayer(request):
    if request.method == 'GET':
        return JsonResponse(User_Game(), safe=False)


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
