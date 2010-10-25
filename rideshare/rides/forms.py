# -*- coding: utf-8 -*-
"""mwGm"""

from django import forms
from rideshare.rides.models import User

DEST_CHOICES = [
                 ('Ann Arbor', 'Ann Arbor'),
                 ('DTW', 'DTW'),
               ]
class AddUserForm(forms.Form):
    fname       = forms.CharField(max_length=30, label="First Name")
    lname       = forms.CharField(max_length=40, label="Last Name")
    uniquename  = forms.CharField(max_length=30, label="Uniquename")
    email       = forms.EmailField(max_length=30, label="Email")
    
    
    
class AddRideForm(forms.Form):
    date        = forms.DateField()
    dest        = forms.ChoiceField(choices=DEST_CHOICES)
    uniquename  = forms.CharField(max_length=30)
    space       = forms.IntegerField()
    note        = forms.CharField(max_length=500, required=False, widget=forms.Textarea)
    
    def clean_uniquename(self):
        un = self.cleaned_data['uniquename']
        try:
            driver = User.objects.get(uniquename=un)
        except User.DoesNotExist:
            raise forms.ValidationError("Unknown uniquename. Are you registered?")
        return un
        
        
class FindRideForm(forms.Form):
    date        =forms.DateField()
    dest        =forms.ChoiceField(choices=DEST_CHOICES)

    
