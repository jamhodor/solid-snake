from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.

def blog(request):
    all_posts = Post.objects.all()
    number_posts = Post.objects.all().count()
    context = {
        "active": "blog",
        "posts": all_posts,
        "nposts": number_posts,
    }
    return render(request, 'blog/blog.html', context)

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        "active": "blog",
        "post": post,
        
    }
    return render(request, 'blog/blog_detail.html', context)