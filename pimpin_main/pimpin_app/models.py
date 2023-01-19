from django.db import models

# Create your models here.

class Message(models.Model):
    '''A message object will have a user id, first and last name field, user info field, and meeting time and place field'''
    # message id will be auto created for me
    # user_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_info = models.CharField(max_length=200)
    meeting_time = models.DateTimeField(
        max_length=16)
    meeting_place = models.CharField(
         max_length=100)
    def __str__(self) -> str:
        return self.name



class Tag(models.Model):
    """Tags that identify or describe a pet"""

    # Descriptive tag 
    body = models.TextField(max_length= 25,help_text="Descriptive Tag")
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.body
