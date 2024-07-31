from django.shortcuts import render
from django.http import HttpResponse
from Core01.templets import *
from Core01.models import Post
def home(request):
    #return HttpResponse("hi this is the home page")
    #load the post data from the database
    posts=Post.objects.all()[:11]
    title = Post.objects.all()[:11]
    print(posts)
    data={
        'posts':posts,
        'title':title,
    }
    return render(request,'home.html',data)


def post(request,title):
    post=Post.objects.get(url=title)
    #print(post)
    #return HttpResponse(title)
    data={'post':post,}
    return render(request, 'post.html',data)


def user(request):
    #return HttpResponse("user page")
    return render(request,'user.html',{})