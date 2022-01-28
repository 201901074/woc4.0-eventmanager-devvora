"""eventmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.conf.urls import url
from enroll import views
from django.urls import path, re_path, include

urlpatterns = [
    re_path(r'^$' , views.index, name='index'),
    re_path(r'^index.html' , views.index, name='index'),
    re_path(r'^event_registration.html', views.regis, name="regis"),
    re_path(r'^event_participation.html', views.parti, name="parti"),
    re_path(r'^event_dashboard.html', views.dash, name="dash"),
    re_path(r'^invalid.html', views.regis, name="regis"),    


]
