from cProfile import label
from django.db import models
from django import forms
import datetime

# Create your models here.


class reg(models.Model):
    hname = models.CharField(max_length=256)
    hemail = models.EmailField()
    ename = models.CharField(max_length=256)
    eloc = models.CharField(max_length=256)
    edesc = models.TextField()
    pswd = models.CharField(max_length=256)
    sdate = models.DateField()
    stime = models.TimeField()
    edate = models.DateField()
    etime = models.TimeField()
    rdate = models.DateField()
    rtime = models.TimeField()
    

class part(models.Model):
    fname = models.CharField(max_length=256)
    lname = models.CharField(max_length=256)
    iemail = models.EmailField()
    icon = models.CharField(max_length=256)
    rtpye = models.CharField(max_length=256,null=True)
    rno = models.PositiveIntegerField()
    eid = models.CharField(max_length=256)


class das(models.Model):
    eid = models.CharField(max_length=256)
    epass = models.CharField(max_length=256)
    
