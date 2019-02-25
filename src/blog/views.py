from django.shortcuts import render, get_object_or_404
from blog.models import Post, Event

# Create your views here.

def blog(request):
    all_posts = Post.objects.all().order_by('-posted_on')
    all_events = Event.objects.all().order_by('-posted_on')
    number_posts = Post.objects.all().count()
    context = {
        "active": "blog",
        "posts": all_posts,
        "nposts": number_posts,
        "events": all_events,
    }
    return render(request, 'blog/blog.html', context)

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    all_events = Event.objects.all().order_by('-posted_on')
    context = {
        "active": "blog",
        "post": post,
        "events": all_events,
    }
    return render(request, 'blog/blog_detail.html', context)