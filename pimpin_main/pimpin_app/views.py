from django.shortcuts import redirect, render
from django.views import View
from pimpin_app.models import Message
from pimpin_app.forms import MessageForm

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='index.html',
        )

class FureverView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='furever.html',
            context={}
        )


class PawfrenceView(View):
    def get(self, request):
        message_form = MessageForm()
        messages= Message.objects.all()

        html_data = {
            'conversation': messages,
            'form': message_form,
        }

        return render(
            request=request,
            template_name='pawfrence.html',
            context=html_data,
        )

    def post(self, request):
        message_form = MessageForm(request.POST)
        message_form.save()

        return redirect('pawfrence')


class MessageDetailView(View):
    def get(self, request, message_id):
        message = Message.objects.get(id=message_id)
        
        message_form = MessageForm(instance=message)

        html_data = {
            'conversation_object': message,
            'form': message_form,
        }

        return render(
            request=request,
            template_name='message_detail.html',
            context=html_data,
        )

    def post(self, request, message_id):
        message = Message.objects.get(id=message_id)
        
        if 'update' in request.POST:
            message_form = MessageForm(request.POST, instance=message)
            message_form.save()
        elif 'delete' in request.POST:
            message.delete()
            
        print(request.POST)

        return redirect('pawfrence')

