from django.shortcuts import redirect, render
from django.views import View
from pimpin_app.models import Message, Tag, Post
from pimpin_app.forms import MessageForm, TagForm, PostForm

# Create your views here.
class HomeView(View):
    ''' HomeView functions as the site's homepage, displaying two different pages and a brief introduction of the two'''
    def get(self, request):
        '''The content required to render the homepage'''
        return render(
            request=request,
            template_name='index.html',
        )

class PawfrenceView(View):
    '''PawfrenceView functions as the site's meetup message page, listing out all the Message objects in the database displayed as contacts and linking out to each one's detail view'''
    def get(self, request):
        '''The content required to render the pawfrence page'''
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
        '''This method saves new Tasks to the database before redirecting to the `get` method of the pawfrence page'''
        message_form = MessageForm(request.POST)
        message_form.save()

        return redirect('pawfrence')


class MessageDetailView(View):
    '''MessageDetailView provides the ability to update and delete individual Message objects from the database'''
    def get(self, request, message_id):
        '''The content required to render a Message object's detail page'''
        message = Message.objects.get(id=message_id)
        message_form = MessageForm(instance=message)

        tags = Tag.objects.filter(message=message)
        tag_form = TagForm(message_object=message)

        html_data = {
            'conversation_object': message,
            'form': message_form,
            'tag_list': tags,
            'tag_form': tag_form,
        }

        return render(
            request=request,
            template_name='message_detail.html',
            context=html_data,
        )

    def post(self, request, message_id):
        '''This method either updates or deletes existing Message objects in the database (depending on user choice), or adding Tag objects before 
        redirecting to the 'get' method of the pawfrence view'''
        message = Message.objects.get(id=message_id)
        
        if 'update' in request.POST:
            message_form = MessageForm(request.POST, instance=message)
            message_form.save()
        elif 'delete' in request.POST:
            message.delete()
        elif 'add' in request.POST:
            tag_form = TagForm(request.POST, message_object=message)
            tag_form.save()

            return redirect('message_detail', message.id)

        # print(request.POST) -used to figure how to specify which button the user clicked

        return redirect('pawfrence')

class FureverView(View):
    def get(self, request):
        post_form = PostForm()
        posts = Post.objects.all()

        html_data = {
            'thread' : posts,
            'form' : post_form
        }
        return render(
            request=request,
            template_name='furever.html',
            context= html_data
        )
    
    def post(self, request):
        post_form = PostForm(request.POST)
        post_form.save()

        return redirect('furever')