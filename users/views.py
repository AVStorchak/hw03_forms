from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from posts.models import Post
from .forms import CreationForm, ContactForm, PostForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


def user_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('/thank-you/')
        return render(request, 'contact.html', {'form': form})
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def new_post(request):
    if request.method == 'POST':
        user = request.user
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(author=user,
                                       text=form.cleaned_data['text'],
                                       group=form.cleaned_data['group'])
            post.save()
            return redirect('/')

    form = PostForm()
    return render(request, "new_post.html", {'form': form})
