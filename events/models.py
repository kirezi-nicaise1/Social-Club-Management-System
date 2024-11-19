from django.db import models
from membership.models import Member

# Create your models here.
from django.db import models

class Event(models.Model):
    event_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    attendees = models.ManyToManyField(Member, related_name="events", blank=True) 

    def __str__(self):
        return self.title
