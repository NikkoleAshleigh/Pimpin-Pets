from django.forms import ModelForm
from django import forms

from pimpin_app.models import Message, Tag, Post


class MessageForm(ModelForm):
    '''Pull the `first_name`, `last_name`,  `user_info`, `meeting_time`, and  `meeting_place`, comlumns from the Message model into a form '''

    class Meta:
        model = Message
        widgets = {
            'first_name': forms.TextInput(attrs={'size': 38, 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'size': 38, 'placeholder': 'Last Name'}),
            'user_info': forms.EmailInput(attrs={'size': 38, 'placeholder': 'Email'}),
            'meeting_time': forms.DateTimeInput(attrs={'size': 38, 'placeholder': 'YYYY-MM-DD HH:MM'}),
            'meeting_place': forms.TextInput(attrs={'size': 38, 'placeholder': 'Specific location'}),
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
    '''Pull the `first_name`, `last_name`,  `pet_info`, and  `home_info` comlumns from the Post model into a form '''
    class Meta:
        model = Post
        widgets = {
            'first_name': forms.TextInput(attrs={'size': 38}),
            'last_name': forms.TextInput(attrs={'size': 38}),
            'pet_info': forms.TextInput(attrs={'size': 38}),
            'home_info': forms.TextInput(attrs={'size': 38}),
            }
        fields = [
            'first_name',
            'last_name',
            'pet_info',
            'home_info',
            'img',
            ]
