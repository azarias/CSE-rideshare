# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.shortcuts import render_to_response
from django.template import RequestContext


from rideshare.rides.forms import *
from rideshare.rides.models import *

pages = {	'addride'	:'addride_form.html',
			'signup'	:'adduser_form.html',
			'findride'	:'findride_form.html',
			'showrides' :'showrides.html',
			'index'		:'index.html',
			'signedup'	:'signedup.html',
			'duplicate'	:'duplicate.html',
			'message'   :'message.html'
		}

def ShowIndex(request):
    return render_to_response(pages['index'])

def ShowAlreadySignedUp(user):
    return render_to_response(pages['duplicate'],
        {'fname':user.fname, 'lname':user.lname})
     
def ShowSignedUp(fname):
    return render_to_response(pages['signedup'], 
        {'fname':fname})
        
def ShowMessage(message):
    return render_to_response(pages['message'],
        {'message':message})
        
def ShowRides(date, dest, rides):
    return render_to_response(pages['showrides'],
        {'date':date, 'dest':dest, 'rides':rides})
        
        
        
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user = User.objects.get(uniquename=cd['uniquename'])
                return ShowAlreadySignedUp(user)
            except User.DoesNotExist:
                User.objects.create(fname=cd['fname'], lname=cd['lname'], email=cd['email'],
                                    uniquename=cd['uniquename'], karma=0)
                return ShowSignedUp(cd['fname'])
    else:
        form = AddUserForm(initial={'email':'@umich.edu'})
        
    return render_to_response(pages['signup'], {'form': form})
    
def add_ride(request):
    if request.method == 'POST':
        form = AddRideForm(request.POST)
        if form.is_valid():                     #checks if driver exists. Can be better.
            cd = form.cleaned_data              
            try:
                dude = User.objects.get(uniquename=cd['uniquename'])
                Ride.objects.create(date=cd['date'], dest=cd['dest'], driver=dude,
                                    space=cd['space'],note=cd['note'], requested=0)
                dude.karma = dude.karma + 1
                dude.save()
                return ShowMessage("Your ride is added. Thank you.")
            except:
                return ShowMessage("There was an error with your request.")     #WTF?
    else:
        form = AddRideForm(initial={'date':'MM/DD/YYYY', 'note':'Flight info, time etc.'})
        
    return render_to_response(pages['addride'], {'form':form})
    
def find_ride(request):
    if len(request.GET) > 0:
        form = FindRideForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            rides = Ride.objects.filter(date=cd['date'],dest=cd['dest'])
            return ShowRides(str(cd['date']),cd['dest'], rides)
    else:
        form = FindRideForm(initial={'date':'MM/DD/YYYY'})
    return render_to_response(pages['findride'], {'form':form})
