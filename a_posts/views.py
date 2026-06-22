from django.shortcuts import render
from .models import *
from django.forms import ModelForm

def home_view(request):
    #print(request.META)
    #print(request.method)
    
    #title = 'Awesome Photos & Captions'
    #return render(request, 'index.html', {'title': title})
    
    posts = Post.objects.all()
    return render(request, 'a_posts/home.html', {'posts':posts})

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'body':'Caption',
        }

def post_create_view(request):
    form=PostCreateForm()
    return render(request, 'a_posts/post_create.html', {'form':form})