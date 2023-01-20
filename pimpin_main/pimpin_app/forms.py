from django.forms import ModelForm
from django import forms

from pimpin_app.models import Message, Tag


class MessageForm(ModelForm):
    '''Pull the `first_name`, `last_name`,  `user_info`, `meeting_time`, and  `meeting_place`, comlumns from the Message model into a form '''

    class Meta:
        model = Message
        widgets = {
            'first_name': forms.TextInput(attrs={'size': 115, 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'size': 114, 'placeholder': 'Last Name'}),
            'user_info': forms.EmailInput(attrs={'size': 114, 'placeholder': 'Email'}),
            'meeting_time': forms.DateTimeInput(attrs={'size': 112, 'placeholder': 'YYYY-MM-DD HH:MM'}),
            'meeting_place': forms.TextInput(attrs={'size': 113, 'placeholder': 'Specific location'}),
            }
        fields = [
            'first_name',
            'last_name',
            'user_info',
            'meeting_time',
            'meeting_place'
            ]


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['body']
    def __init__(self, *args,**kwargs):
        message = kwargs.pop('message_object')
        super().__init__(*args,**kwargs)
        # This needs to be created still on a seperate view
        self.instance.message = message
        self.fields['body'].label=''