from django.shortcuts import render
from django.http import HttpResponse
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'rank/home.html', context)

def about(request):
    return render(request, 'rank/about.html', {'title': 'About'})
