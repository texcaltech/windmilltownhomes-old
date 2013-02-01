from django.core.cache import cache
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from guestbook.forms import CreateGreetingForm
from guestbook.models import Greeting

#MEMCACHE_GREETINGS = 'greetings'

def home(request):
    #home = cache.get(MEMCACHE_HOME)
    return direct_to_template(request, 'home.html')