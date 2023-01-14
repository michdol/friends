from django.urls import path

from posts.views import PostCreateView, PostListView


urlpatterns = [
    path('list/<username>/', PostListView.as_view(), name='posts'),
    path('create/', PostCreateView.as_view(), name='create'),
]