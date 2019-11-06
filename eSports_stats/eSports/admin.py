from django.contrib import admin
import eSports.models as models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Role)
admin.site.register(models.Staff)
admin.site.register(models.Status)
admin.site.register(models.Player)
admin.site.register(models.Game)
admin.site.register(models.Team_Rank)
admin.site.register(models.Team)
admin.site.register(models.user_team)
admin.site.register(models.Stats)
admin.site.register(models.user_game)
