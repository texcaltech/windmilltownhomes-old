from django.conf.urls.defaults import *

urlpatterns = patterns('windmilltownhomes.views',
    (r'^floor-plans/', 'floor_plans'),
    (r'^pre-lease/', 'pre_lease'),
    (r'^$', 'home')
)