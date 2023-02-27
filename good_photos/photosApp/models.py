from django.db import models

# Create your models here.

class User(models.Model):
    user_id= models.PositiveIntegerField()
    user_name = models.CharField(max_length=200)
class Subscriber(models.Model):
    subscriber_id = models.PositiveIntegerField()
    subscriber_name = models.ForeignKey