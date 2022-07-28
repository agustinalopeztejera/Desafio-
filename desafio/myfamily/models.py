
from django.db import models
from django.forms import DateTimeField
import datetime 

class Family_members(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    hobbies = models.CharField(max_length=60)
    last_active_whapp = DateTimeField(datetime.now)

