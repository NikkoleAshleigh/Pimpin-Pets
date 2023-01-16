from django.forms import ModelForm

from pimpin_app.models import Message, Tag

class MessageForm(ModelForm):
    '''Pull the `user_id`, `first_name`, `last_name`,  `user_info`, `meeting_time`, and  `meeting_place`, comlumns from the Message model into a form '''
    class Meta:
        model = Message
        fields = ['first_name', 'last_name', 'user_info', 'meeting_time', 'meeting_place']


class TagForm(ModelForm):
    '''Pull the `body` comlumn from the Tag model into a form '''
    class Meta:
        model = Tag
        fields = ['body']

    def __init__(self, *args, **kwargs):
        message = kwargs.pop('message_object')
        super().__init__(*args, **kwargs)

        self.instance.message = message