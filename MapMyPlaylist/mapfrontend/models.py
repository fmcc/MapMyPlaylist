from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    lastfmusername = models.CharField(max_length=200)
    def __unicode__(self):
        return self.user.username

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['lastfmusername']


