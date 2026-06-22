from django.shortcuts import render
from .models import *

def home_view(request):
    #print(request.META)
    #print(request.method)
    
    #title = 'Awesome Photos & Captions'
    #return render(request, 'index.html', {'title': title})
    
    posts = Post.objects.all()
    return render(request, 'a_posts/home.html', {'posts':posts})