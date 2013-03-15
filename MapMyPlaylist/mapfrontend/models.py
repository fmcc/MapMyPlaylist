from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from findartist.models import Location

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    lastfmusername = models.CharField(max_length=200)
    currentlocation = models.ForeignKey(Location, blank=True, null=True)
    friends = models.ManyToManyField('UserProfile', blank=True, null=True)
    def __unicode__(self):
        return self.user.username

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['lastfmusername']

