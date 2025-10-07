from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from django.urls import path
from .views import PostSearchView

from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    # Post URLs
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]


urlpatterns += [
    path('search/', PostSearchView.as_view(), name='post-search'),
    path('tags/<slug:tag_slug>/', PostListView.as_view(), name='posts-by-tag'),  # filtered by tag
]