from cProfile import label
from django.db import models
# from django.utils.encoding import force_text
from django import forms
# from django.forms import DateField, widgets
# from django.utils import format
# from datetimepicker.widgets import DateTimePicker
# from datetime import datetime

# Create your models here.


class reg(models.Model):
    hname = models.CharField(max_length=256)
    hemail = models.EmailField()
    ename = models.CharField(max_length=256)
    eloc = models.CharField(max_length=256)
    edesc = models.TextField()
    pswd = models.CharField(max_length=256, default="pswd")
    sdate = models.DateField()
    stime = models.TimeField()
    edate = models.DateField()
    etime = models.TimeField()
    rdate = models.DateField()
    rtime = models.TimeField()
    
    
