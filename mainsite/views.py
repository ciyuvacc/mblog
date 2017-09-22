from django.shortcuts import render,redirect
from django.template.loader import get_template

# Create your views here.
from django.http import HttpResponse
from .models import Post
from datetime import datetime


def homepage1(request):
    posts = Post.objects.all()
    post_lists = list()
    for count,post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
    return HttpResponse(post_lists)

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now
    html = template.render(locals())
    return HttpResponse(html)


def showpost(request,slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
