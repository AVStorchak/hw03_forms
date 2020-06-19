import datetime
from django.shortcuts import render, get_object_or_404

from .models import Group, Post, User


def index(request):
    posts = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})
