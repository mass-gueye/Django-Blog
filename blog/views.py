from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def index(request):
    latest_post = Post.objects.last()
    context = {
        'message': 'Welcome to my hood.',
        'latest_post': latest_post,

    }
    return render(request, "index.html", context)

def posts(request):
    

    context = {
        'message': 'All Posts.',
        'posts': Post.objects.all(),
        # 'username': User.username
    }
    return render(request, "posts.html", context)


def post(request):
    posts = []
    context = {
        'message': 'All Posts.',
        'posts': posts,

    }
    return render(request, "post.html", context)


def post_details(request, details):
    context = {
        'message': 'Details post.',
        'slug':details,
        'post_details': get_object_or_404(Post, slug=details),
        'post_tags': get_object_or_404(Post, slug=details).tags.all()
    }

    return render(request, "post-details.html", context)

