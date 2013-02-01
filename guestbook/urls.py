from django.conf.urls.defaults import *

urlpatterns = patterns('guestbook.views',
    (r'^$', 'home')
)