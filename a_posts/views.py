from django.shortcuts import render

def home_view(request):
    #print(request.META)
    #print(request.method)
    
    #title = 'Awesome Photos & Captions'
    #return render(request, 'index.html', {'title': title})
    
    return render(request, 'includes/a_posts/home.html')