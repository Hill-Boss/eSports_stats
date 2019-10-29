from django.db import models

# TODO: Change Char Lengths
# class User(models.Model):
#     user_id = models.IntegerField(primary_key=True)
#     login_name = models.CharField(max_length=60)
#     first_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)
#     email = models.EmailField(max_length=60)
#     discord = models.CharField(max_length=60)
#
# class Role(models.Model):
#     role_id = models.IntegerField(primary_key=True)
#     role_name = models.CharField(max_length=60)
#
# class Staff(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
#     role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
#     status = models.BooleanField()
#     date_start = models.DateField()
#     date_end = models.DateField()
#
# class Status(models.Model):
#     status_id = models.IntegerField(primary_key=True)
#     status = models.CharField(max_length=60)
#     date_start = models.DateField()
#     date_end = models.DateField()
#
# class Player(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
#     status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
#     student_id = models.IntegerField()
#     pga = models.PositiveSmallIntegerField()
#     YEAR_IN_SCHOOL_CHOICES = [
#     ('FR', 'Freshman'),
#     ('SO', 'Sophmore'),
#     ('JR', 'Junior'),
#     ('SR', 'Senior'),
#     ]
#     year = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)
#     major = models.CharField(max_length=60)
#     date_start = models.DateField()
#     date_end = models.DateField()
#
# class Game(models.Model):
#     game_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=60)
#     status = models.CharField(max_length=60) # TODO: change??
#     platform = models.CharField(max_length=60)
#     launcher = models.CharField(max_length=60)
#
# class Team_Rank(models.Model):
#     rank_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=60)
#
# class Team(models.Model):
#     team_id = models.IntegerField(primary_key=True)
#     game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
#     rank_id = models.ForeignKey(Game, on_delete=models.CASCADE)
#     status = models.CharField(max_length=60)
#     team_name = models.CharField(max_length=60)
#     date_start = models.DateField()
#     date_end = models.DateField()
#
# class user_team(models.Model):
#     user_id = models.ForeignKey(Player, on_delete=models.CASCADE, primary_key=True)
#     team_id = models.ForeignKey(Team, on_delete=models.CASCADE, primary_key=True)
#     team_cap = models.BooleanField()
#     date_start = models.DateField()
#     date_end = models.DateField()
#
# class Stats(models.Model):
#     stat_id = models.IntegerField(primary_key=True)
#     stats = models.TextField() # TODO: JSON OR SOMETHING
#     date_updated = models.DateTimeField(auto_now=True)
#
# class user_game(models.Model):
#     user_id = models.ForeignKey(Player, on_delete=models.CASCADE, primary_key=True)
#     game_id = models.ForeignKey(Game, on_delete=models.CASCADE, primary_key=True)
#     stat_id = models.ForeignKey(Stats, on_delete=models.CASCADE)
#     username = models.CharField(max_length=60)
