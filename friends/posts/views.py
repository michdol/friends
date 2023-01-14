from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.urls import reverse

from posts.forms import PostForm
from posts.models import Post
from users.models import User


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(user__username=user.username)

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)

        username = self.kwargs.get('username')
        context['posts'] = Post.objects.filter(user__username=username)
        context['username'] = username
        return context


class PostCreateView(FormView):
    template_name = 'posts/post_create.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('posts:posts', kwargs={'username': self.request.user.username})
