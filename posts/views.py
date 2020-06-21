from django.shortcuts import render, redirect, get_object_or_404

from posts.models import Post
from posts.forms import PostForm
from .models import Group, Post


def index(request):
    posts = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')

    form = PostForm()
    return render(request, "new_post.html", {'form': form})
