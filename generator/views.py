from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random
# Create your views here.
def home(request):
    now = datetime.datetime.now()
    display_time = "It is now %s." % now
    characters = list('abcdefghijklmnopqrstuvwxyz')
    submit = request.GET.get('submit')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    length = int(request.GET.get('length',12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    context = {'password':thepassword,
                'submit':submit
    }
    return render(request, 'generator/home.html', context )

def password(request):
    password = 'test'
    return render(request,"generator/password.html", {'password':password})
