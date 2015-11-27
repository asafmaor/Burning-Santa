from django.contrib.auth.models import User as AuthUser
from midburn.santa.models import User
import json
__author__ = 'safo'


def _create_new_user_object(email, password, username=None):
    username = username if username else email
    return AuthUser.objects.create_user(username, email, password)


def create_new_user(first_name, last_name, playa_name, email, password, city, address, zipcode, is_willing_to_get):
    django_user = _create_new_user_object(email, password)
    User = User()


def is_request_post(r, *kargs):
    if not r.method == 'POST':
        return False

    for o in kargs:
        if not o in r.POST or len(r.POST[o]) == 0:
            return False

    return True


def jun_post(r):
    if is_request_post(r):
        return r.POST


def post_to_json(r):
    j = jun_post(r)
    if j:
        return json.loads(j['json'])