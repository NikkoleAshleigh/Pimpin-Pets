from django.forms import ModelForm

from pimpin_app.models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['user_id', 'first_name', 'last_name', 'user_info', 'meeting_time', 'meeting_place']