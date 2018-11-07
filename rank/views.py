from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Jchaszar',
        'title': 'Rank posting 1',
        'content': '...',
        'date_posted': 'November 6, 2018'
    },
    {
        'author': 'John Smith',
        'title': 'Rank posting 2',
        'content': '...222',
        'date_posted': 'November 6, 2018'
    }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'rank/home.html', context)

def about(request):
    return render(request, 'rank/about.html', {'title': 'About'})
