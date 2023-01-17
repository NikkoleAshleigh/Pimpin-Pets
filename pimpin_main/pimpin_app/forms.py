from django.forms import ModelForm
from django import forms

from pimpin_app.models import Message, Tag

class MessageForm(forms.Form):
    '''Pull the `first_name`, `last_name`,  `user_info`, `meeting_time`, and  `meeting_place`, comlumns from the Message model into a form '''

    class Meta:
        model = Message
        fields = ['first_name', 'last_name', 'user_info', 'meeting_time', 'meeting_place']
    # first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'size': '50'}))
    # last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={'size': '50'}))
    # user_info = forms.CharField(label='Email', max_length=255, widget=forms.TextInput(attrs={'size': '50'}))
    # meeting_time = forms.DateTimeField(
    #     # help_text="YYYY-MM-DD HH:MM",
    #     max_length=16
    # )
    # meeting_place = forms.CharField(label='Meeting Place', max_length=255, widget=forms.TextInput(attrs={'size': '50'}))


class TagForm(ModelForm):
    '''Pull the `body` comlumn from the Tag model into a form '''
    class Meta:
        model = Tag
        fields = ['body']

    def __init__(self, *args, **kwargs):
        message = kwargs.pop('message_object')
        super().__init__(*args, **kwargs)

        self.instance.message = message