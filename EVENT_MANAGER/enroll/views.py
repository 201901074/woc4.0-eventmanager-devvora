
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