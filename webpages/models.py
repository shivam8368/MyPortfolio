from django.db import models
from datetime import datetime

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=400)
    email = models.CharField(max_length=400)
    subject = models.TextField()
    message = models.TextField(blank=True)

    date_created = models.DateTimeField(blank=True, default=datetime.now)



    def __str__(self):
        return self.name