from django.urls import path

from . import views
from users.views import new_post

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", new_post, name="new_post"),
    path("group/<slug:slug>/", views.group_posts, name="group_posts")
]
