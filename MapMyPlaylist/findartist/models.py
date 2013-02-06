from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=200)
    image  = models.CharField(max_length=200)
    origin = models.ForeignKey('Location')

class Location(models.Model):
    placename = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
