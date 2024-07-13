from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"

class Comment(models.Model):
    event = models.ForeignKey(Event, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField