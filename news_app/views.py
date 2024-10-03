from django.shortcuts import render, get_object_or_404
from .models import Post

def home_page(request):
    posts = Post.objects.all().order_by('-created_at')[:4]
    context = {
        'posts': posts
    }
    return render(request, "home.html", context)

def all_posts_page(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, "posts.html", context)

def post_detail_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, "detail.html", context)