from django.forms import ModelForm
from django import forms

from pimpin_app.models import Message, Tag, Post


class MessageForm(ModelForm):
    '''Pull the `first_name`, `last_name`,  `user_info`, `meeting_time`, and  `meeting_place`, comlumns from the Message model into a form '''

    class Meta:
        model = Message
        widgets = {
            'first_name': forms.TextInput(attrs={'size': 115}),
            'last_name': forms.TextInput(attrs={'size': 114}),
            'user_info': forms.EmailInput(attrs={'size': 114}),
            'meeting_time': forms.DateTimeInput(attrs={'size': 112}),
            'meeting_place': forms.TextInput(attrs={'size': 113}),
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
        # post = kwargs.pop('post_object')
        super().__init__(*args,**kwargs)
        # This needs to be created still on a seperate view
        self.instance.message = message
        # self.instance.post = post
        self.fields['body'].label=''


class PostForm(ModelForm):

    class Meta:
        model = Post
        widgets = {
            'first_name': forms.TextInput(attrs={'size': 115}),
            'last_name': forms.TextInput(attrs={'size': 114}),
            'pet_info': forms.TextInput(attrs={'size': 114}),
            'home_info': forms.TextInput(attrs={'size': 112}),
            }
        fields = [
            'first_name',
            'last_name',
            'pet_info',
            'home_info',
            ]
