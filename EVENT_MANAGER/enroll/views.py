
from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render
from .models import reg

def index(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context,request))


def regis(request):

    if request.method == "POST":
        obj = reg()
        obj.hname = request.POST('hname')
        obj.hemail = request.POST('hemail')
        obj.ename = request.POST('ename')
        obj.eloc = request.POST('eloc')
        obj.pswd = request.POST('pswd')
        obj.edesc = (request.POST('edesc'))
        obj.sdate = (request.POST('fromd'))
        obj.stime = (request.POST('fromt'))
        obj.edate = (request.POST('tod'))
        obj.etime = (request.POST('tot'))
        obj.rdate = (request.POST('rdd'))
        obj.rtime = (request.POST('rdt'))
        obj.save()

        return render(request, 'index.html')

    else:
        template = loader.get_template('event_registration.html')
        context = {

        }
        return HttpResponse(template.render(context,request))

    
def parti(request):
    data = reg.objects.all()
    return render(request, 'event_participation.html' ,{'data':data})
    template = loader.get_template('event_participation.html')
    context = {

    }
    return HttpResponse(template.render(context,request))

    
def dash(request):
    data = reg.objects.all()
    return render(request, 'event_dashboard.html' ,{'data':data})