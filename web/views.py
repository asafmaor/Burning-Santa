from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login, logout, authenticate
from web.utils.web import is_request_post

__author__ = 'safo'

@csrf_exempt
def login_view(request):
    error = None
    if is_request_post(request):
        post_data = request.POST
        user = authenticate(
            username=post_data['email'],
            password=post_data['password']
        )

        if user and user.is_active:
            print "logged in"
            if request:
                login(request, user)
            return redirect('welcome')
        print "failed login"
        error = 'Could not login. please make sure the information is correct.'

    return render(request, 'web/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('welcome')


def register(request):
    if not is_request_post(request):
        render()


def welcome(request):
    is_logged_in = request.user.is_authenticated()
    return render(request, 'web/welcome.html', {'logged_in': is_logged_in})
