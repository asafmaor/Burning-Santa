from django.conf.urls import patterns, url
__author__ = 'safo'
urlpatterns = patterns('web.views',
    url(r'^$', 'welcome', name='welcome'),
    url(r'^login/$', 'login_view', name='login_user'),
    url(r'^register/$', 'register', name='register_user'),
    url(r'^logout/$', 'logout_view', name='logout_user')
 )
