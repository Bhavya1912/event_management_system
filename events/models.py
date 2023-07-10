from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    categories = models.ManyToManyField('Category', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'events'
class Category(models.Model):
    name = models.CharField(max_length=255)

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, default='Pending')

class Venue(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    amenities = models.TextField()
    availability = models.BooleanField(default=True)

# Add any additional fields to the User model as needed
