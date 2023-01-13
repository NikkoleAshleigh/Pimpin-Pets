from django.db import models

# Create your models here.

class Message(models.Model):
    '''A message object will have a user id, first and last name field, user info field, and meeting time and place field'''
    # message id will be auto created for me
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_info = models.CharField(max_length=200)
    meeting_time = models.DateTimeField()
    meeting_place = models.CharField(max_length=100)
    