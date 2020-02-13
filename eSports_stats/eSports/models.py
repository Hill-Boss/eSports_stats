from django.db import models
from django.contrib.auth.models import User as user_account

# TODO: Change Char Lengths
class User(models.Model):
    # login_name = models.CharField(max_length=60)
    # first_name = models.CharField(max_length=60)
    # last_name = models.CharField(max_length=60)
    # email = models.EmailField(max_length=60)
    user_id = models.OneToOneField(user_account, primary_key=True, on_delete=models.CASCADE)
    discord = models.CharField(max_length=60, default=None, blank=True, null=True)

    def __str__(self):
        return self.user_id.username


class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=60)

    def __str__(self):
        return self.role_name


class Staff(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    status = models.BooleanField()
    date_start = models.DateField()
    date_end = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.user_id.user_id.username


class Status(models.Model):
    status_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=60)
    date_start = models.DateField()
    date_end = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.status


class Player(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    student_id = models.IntegerField()
    gpa = models.PositiveSmallIntegerField()
    YEAR_IN_SCHOOL_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophmore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('UN', 'Unknown'),
        ('NA', 'Not Applicable'),
    ]
    year = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)
    major = models.CharField(max_length=60)
    date_start = models.DateField()
    date_end = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.user_id.user_id.username


class Game(models.Model):
    game_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    status = models.CharField(max_length=60) # TODO: change??
    platform = models.CharField(max_length=60)
    launcher = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Team_Rank(models.Model):
    rank_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    rank_id = models.ForeignKey(Team_Rank, on_delete=models.CASCADE)
    status = models.CharField(max_length=60)
    team_name = models.CharField(max_length=60)
    date_start = models.DateField()
    date_end = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.team_name


class user_team(models.Model):
    user_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user_id', 'team_id')
    team_cap = models.BooleanField()
    date_start = models.DateField()
    date_end = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return (self.team_id.team_name + ", " + self.user_id.user_id.user_id.username)


class Stats(models.Model):
    stat_id = models.AutoField(primary_key=True)
    stats = models.TextField() # TODO: JSON OR SOMETHING
    date_updated = models.DateTimeField(auto_now=True)

# TODO: str return???
    # def __str__(self):
    #     return self.SOMETHING


class user_game(models.Model):
    user_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user_id', 'game_id')
    stat_id = models.ForeignKey(Stats, on_delete=models.CASCADE, default=None, blank=True, null=True)
    username = models.CharField(max_length=60)

    def __str__(self):
        return (self.game_id.name + ", " + self.user_id.user_id.user_id.username)
