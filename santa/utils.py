from django.contrib.auth.models import User as AuthUser
from midburn.santa.models import User
import json
__author__ = 'safo'


def _create_new_user_object(email, password, username=None):
    username = username if username else email
    return AuthUser.objects.create_user(username, email, password)




