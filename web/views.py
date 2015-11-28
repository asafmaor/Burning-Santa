from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from web.utils.web import is_request_post
from web.utils.users import authenticate_midburn, register_new_user

from santa.models import SantaUser

__author__ = 'safo'

@csrf_exempt
def login_view(request):
    error = None
    if not is_request_post(request):
        return render(request, 'web/login.html', {'error': error})
    post_data = request.POST
    username = post_data.get('email')
    password = post_data.get('password')

    user = authenticate(
        username=post_data['email'],
        password=post_data['password']
    )
    is_midburn_user = authenticate_midburn(username, password)
    if not is_midburn_user:
        error = "You are not a true burner!"
        return render(request, 'web/login.html', {'error': error})

    if is_midburn_user and not user:
        user, created = User.objects.get_or_create(username=username)
        user.email = username
        user.set_password(password)
        user.is_active = True
        user.save()
        user = authenticate(username=username,password=password)
        print user

    try:
        s_user = SantaUser.objects.get(django_user_id=user.id)
    except SantaUser.DoesNotExist:
        s_user = SantaUser()
        s_user.django_user = user
        s_user.email = user.email
        s_user.is_signed_in = False
        s_user.save()

    if user and user.is_active:
        print "logged in"
        login(request, user)

        if s_user.is_signed_in:
            return redirect('welcome')
        return redirect('register_user')

    return render(request, 'web/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login_user')

@login_required()
def register(request):
    if not is_request_post(request):
        return render(request, 'web/register.html')
    post_data = request.POST
    santa_user = SantaUser.objects.get(email=request.user.email)
    register_new_user()

@login_required()
def welcome(request):
    is_logged_in = request.user.is_authenticated()
    return render(request, 'web/welcome.html', {'logged_in': is_logged_in})
