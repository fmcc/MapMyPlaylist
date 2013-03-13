from django.contrib.auth.models import User
from mapfrontend.models import UserProfile, UserForm, UserProfileForm
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from registration.forms import RegistrationForm

def mainpage(request):
    return render_to_response('MMP_base.html')

def userpage(request, username):
    try:
        user = UserProfile.objects.get(user = User.objects.get(username = username))
    except User.DoesNotExist:
        print "unknownuser"
    return render_to_response('MMP_user.html', {'user': user })

"""
def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        uform = UserForm(data = request.POST)
        pform = UserProfileForm(data = request.POST)
        if uform.is_valid() and pform.is_valid():
            user = uform.save()
            pw = user.password
            user.set_password(pw)
            user.save()
            profile = pform.save(commit = False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print uform.errors, pform.errors
    else:
        uform = UserForm()
        pform = UserProfileForm()


    return render_to_response('register.html', {'uform': uform, 'pform': pform, 'registered': registered }, context)
"""
def register(request):
    login_form = UserForm
    return render_to_response('register.html', {"login_form" : login_form})

def ajaxLogin(request):
    print "Requested"
    if request.method == 'POST':
        print len(request.POST)
    else:
        "print"


