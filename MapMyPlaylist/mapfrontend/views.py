from django.contrib.auth.models import User
from mapfrontend.models import UserProfile, UserForm, UserProfileForm
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.forms import AuthenticationForm
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
    form = UserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            if request.is_ajax: 
                user = authenticate(username = request.POST['username'],password = request.POST['password'])
                if user is not None:
                    redirect_to = '/home/%s/'%user
                else:
                    print "User unknown"
        else:
            print "Wrong username/password"

    obj = {
        'userprofile': UserForm(),
    }
    return render(request, 'register.html', obj)
