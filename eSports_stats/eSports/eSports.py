from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import User, Role, Staff, Status, Player, Game, Team_Rank, Team, user_team, Stats, user_game


# def {{'Get some data table data'}}():
#     all_{{'data'}} = {{'data table name'}}.objects.all()
#     all_{{'data'}} = encoder_JSON(all_{{'data'}})
#     return all_{{'data'}}
#
# # create uncoder for table
# def JSON_encoder_{{'table name'}}(data):
#     response = {}
#     for key in data:
#         obj = []
#         obj.append({{'table.Stuff'}})
#         response[key.{{'table identifier'}}] = obj
#     return response
