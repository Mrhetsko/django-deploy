from django.shortcuts import render
from .models import Posts


def index(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)
