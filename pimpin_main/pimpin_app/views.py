from django.shortcuts import redirect, render
from django.views import View
from pimpin_app.models import Message, Tag, Post, Pets
from pimpin_app.forms import MessageForm, TagForm, PostForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 


class HomeView(View):
    ''' HomeView functions as the site's homepage, displaying a brief introduction of the two'''
    def get(self, request):
        '''The content required to render the homepage'''
        return render(
            request=request,
            template_name='index.html',
        )

class PawfrenceView(View):
    '''PawfrenceView functions as the site's meetup message page, listing out all the Message objects in the database displayed as contacts and linking out to each contact's detail view'''
    def get(self, request):
        '''The content required to render the pawfrence page'''
        message_form = MessageForm()
        messages= Message.objects.all()

        html_data = {
            'message_list': messages,
            'form': message_form,
        }

        return render(
            request=request,
            template_name='pawfrence.html',
            context=html_data,
        )

    def post(self, request):
        '''This method saves new Tasks to the database before redirecting to the `get` method of the pawfrence page'''
        print(request.POST)
        message_form = MessageForm(request.POST)
        message_form.save()

        return redirect('pawfrence')


class MessageDetailView(View):
    '''MessageDetailView provides the ability to create individual Message objects from the database'''
    def get(self, request, message_id):
        '''The content required to render a Message object's detail page'''
        message = Message.objects.get(id=message_id)
        message_form = MessageForm(instance=message)

        tag = Tag.objects.filter(message_id = message_id)
        # Creates the view for the form
        tag_form = TagForm(message_object = message)


        html_data = {
            'message': message,
            'form': message_form,
            'tag_list': tag,
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
    '''FureverView provides the ability to create individual Post objects from the database'''

    def get(self, request):
        '''The content required to render a Post object's detail page'''
        post_form = PostForm()
        posts = Post.objects.all()
        pets = Pets.objects.all()

        html_data = {
            'thread' : posts,
            'form' : post_form,
            'pets_list': pets,
        }

        return render(
            request=request,
            template_name='furever.html',
            context=html_data,
        )

    def post(self, request):
        post_form = PostForm(request.POST, request.FILES)
        post_form.save()
        instance = post_form.instance

        return redirect('furever')

class NeedingLoveView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post_form = PostForm(instance=post)
        
        # tag = Tag.objects.filter(post_id = post_id)
        # tag_form = TagForm(post_object = post)

        html_data = {
            'post': post,
            'form': post_form,
            
            # 'tag_list' : tag,
            # 'tag_form' : tag_form
        }

        return render(
            request=request,
            template_name= 'needing_love.html',
            context=html_data
        )
    
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)

        if 'update' in request.POST:
            post_form = PostForm(request.POST, instance=post)
            post_form.save()
        elif 'delete' in request.POST:
            post.delete()
        # elif 'add' in request.POST:
            # tag_form = TagForm(request.POST, post_object=post)
            # tag_form.save()
            # return redirect('adoption', post.id)

        return redirect('furever')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('pimpin')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("pimpin")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("pimpin")
