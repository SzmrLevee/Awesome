from django.shortcuts import render

def home_view(request):
    title = 'Awesome Photos & Captions'
    return render(request, 'index.html', {'title': title})