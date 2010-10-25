# -*- coding: utf-8 -*-
"""mwGm"""

from django.db import models

class User(models.Model):
    fname       = models.CharField(max_length=30)
    lname       = models.CharField(max_length=40)
    uniquename  = models.CharField(max_length=30)
    email       = models.EmailField()
    karma       = models.IntegerField()
    
    def __unicode__(self):
        return self.fname + " " + self.lname
    
    
class Ride(models.Model):
    date        = models.DateField()
    dest        = models.CharField(max_length=30)
    driver      = models.ForeignKey(User)
    space       = models.IntegerField()
    note        = models.CharField(max_length=500)  #any note the driver has
    requested   = models.IntegerField()             #a rough count for popularity