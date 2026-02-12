from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.TextField()
    date = models.DateField()
    location = models.TextField()

    def __str__(self):
        return self.name 