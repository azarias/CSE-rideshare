# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('rideshare.rides.views',
	(r'^$', 'ShowIndex'),
	(r'^addride/$', 'add_ride'),
	(r'^findride/$', 'find_ride'),
	(r'^signup/$', 'add_user'),
)
