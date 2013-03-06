from django.contrib.auth.models import User
from mapfrontend.models import UserProfile, UserForm, UserProfileForm
from django.shortcuts import render_to_response

def mainpage(request):
    return render_to_response('MMP_mainpage.html')

def settings(request):
    return render_to_response('MMP_settings.html')


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
        apform = UserProfileForm()

    return render_to_response('rango/register.html', {'uform': uform, 'pform': pform, 'registered': registered }, context)
