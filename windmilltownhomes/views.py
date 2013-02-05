from django.core.cache import cache
from django.views.generic.simple import direct_to_template

def floor_plans(request):
    return direct_to_template(request, 'floor_plans.html')

def home(request):
    return direct_to_template(request, 'home.html')

def pre_lease(request):
    return direct_to_template(request, 'pre_lease.html')