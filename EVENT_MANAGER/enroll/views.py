
from email.policy import HTTP
import re
from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template
from django.shortcuts import redirect, render
from .models import reg, part, das
import datetime
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
from django.contrib import messages



def index(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context,request))


def regis(request):

    if request.method == "POST":
        obj = reg()
        obj.hname = request.POST.get('hname')
        obj.hemail = request.POST.get('hemail')
        obj.ename = request.POST.get('ename')
        obj.eloc = request.POST.get('eloc')
        obj.pswd = request.POST.get('pswd')
        obj.edesc = (request.POST.get('edesc'))
        obj.sdate = (request.POST.get('fromd'))
        obj.stime = (request.POST.get('fromt'))
        obj.edate = (request.POST.get('tod'))
        obj.etime = (request.POST.get('tot'))
        obj.rdate = (request.POST.get('rdd'))
        obj.rtime = (request.POST.get('rdt'))

        if obj.sdate > obj.edate or (obj.sdate == obj.edate and obj.stime > obj.etime):
            return HttpResponse("Please recheck the timings")
        
        clash = reg.objects.filter(ename = obj.ename)

        for e in clash:
            if (str(e.sdate) > obj.edate or str(e.edate) < obj.sdate) or (str(e.sdate)==obj.edate and obj.etime < str(e.stime)) or (str(e.edate) == obj.sdate and str(e.etime) < obj.stime):
                continue
            else:
                return HttpResponse("Please either change the name of your event or its timings.")

        obj.save()

        # send_mail(
        #     'Success',
        #     'Your Event is registered successfully with event id %s' %(reg.objects.latest('id')),
        #     'managerevent15@gmail.com',
        #     [obj.hemail],
        #     fail_silently=False
        # )

        return render(request, 'index.html')

    else:
        template = loader.get_template('event_registration.html')
        context = {

        }
        return HttpResponse(template.render(context,request))

    
def parti(request):

    data = reg.objects.all()
    
    if request.method == "POST":
        obj = part()
        obj.fname = request.POST.get('fname')
        obj.lname = request.POST.get('lname')
        obj.iemail = request.POST.get('iemail')
        obj.icon = request.POST.get('icon')
        obj.eid = request.POST.get('choices')
        obj.rtype = request.POST.get('options')
        if obj.rtype=='indi':
            obj.rno = 1
        else:
            obj.rno = request.POST.get('rno')

        i = part.objects.filter(eid=obj.eid, iemail=obj.iemail)
        if len(i) > 0:
            return render(request, 'invalid.html', {'message':"You have already registered in this event"})

        obj.save();

        ev = reg.objects.get(id=obj.eid)

        # send_mail(
        #     'Success',
        #     'You have registered successfully in the event %s with your contact number %s. Total of exactly %s persons have registered from your side. Your unique event id %s' %(ev.ename, obj.icon, obj.rno, part.objects.latest('id')),
        #     'managerevent15@gmail.com',
        #     [obj.iemail],
        #     fail_silently=False
        # )
        
        # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        # message = client.messages.create(
        #                                 body=f'Dear {obj.fname},\n You have successfully registered in the event {ev.ename} with your contact number {obj.icon}. Total of exactly {obj.rno} persons have registered from your side.\n Venue: {ev.eloc}\nStart Time : {ev.sdate} {ev.stime}\nEnd Time: {ev.edate} {ev.etime}\n For any further queries, please email to {str(ev.hemail)}',
        #                                 from_='+18106349090',
        #                                 to=f'+91{obj.icon}' 
        #                             )
        print(message.sid)
        return render(request, 'index.html')

    else:

        obj = []

        for row in data:
            if datetime.date.today() < row.rdate or (datetime.date.today() == row.rdate and datetime.datetime.now().time() < row.rtime) :
                obj.append(row)

        return render(request, 'event_participation.html' ,{'data':obj })
    
    
def dash(request):

    if request.method == "POST":

        obj = das()
        obj.eid = request.POST.get('hid')
        obj.epass = request.POST.get('epass')

        err = "Invalid Username or Password"
        
        try:
            ev = reg.objects.get(id=obj.eid)                
        except:
            # messages.error(request, 'Invalid username or password')
            return render(request, 'invalid.html', {'message':err})
        print(ev.pswd, obj.epass)
        if ev.pswd != obj.epass:
            # messages.error(request, 'Invalid username or password')
            return render(request, 'invalid.html', {'message':err})
        
        data = part.objects.filter(eid=obj.eid)
        return render(request, 'participant.html' ,{'data':data})

    else:
        return render(request, 'event_dashboard.html')