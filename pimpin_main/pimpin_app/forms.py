from django.forms import ModelForm

from pimpin_app.models import Message

class MessageForm(ModelForm):
    '''Pull the `user_id`, `first_name`, `last_name`,  `user_info`, `meeting_time`, and  `meeting_place`, comlumns from the Message model into a form '''
    class Meta:
        model = Message
        fields = ['first_name', 'last_name', 'user_info', 'meeting_time', 'meeting_place']