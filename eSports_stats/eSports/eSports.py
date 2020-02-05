from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# TODO: This is would allow users to Publish a post for example, might be useful
# from myapp.models import BlogPost
#
# def create_Permissions():
#     content_type = ContentType.objects.get_for_model(BlogPost)
#     permission = Permission.objects.create(
#         codename='can_publish',
#         name='Can Publish Posts',
#         content_type=content_type,
#     )

def auth_user(user, password):
    user = authenticate(username=user, password=password)
    if user is not None:
        pass
        # A backend authenticated the credentials
    else:
        pass
        # No backend authenticated the credentials

def set_password(user, newPass):
    u = User.objects.get(username=user)
    u.set_password(newPass)
    u.save()

def create_user(first, last, email, password):
    u = User.objects.create_user(first, email, password, last_name=last)
    u.save()
