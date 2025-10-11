from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification

User = get_user_model()

# -----------------------------
# Pagination Classes
# -----------------------------
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

class FeedPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

# -----------------------------
# Post ViewSet
# -----------------------------
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'content']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# -----------------------------
# Comment ViewSet
# -----------------------------
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# -----------------------------
# Feed API
# -----------------------------
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def FeedView(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    paginator = FeedPagination()
    paginated_posts = paginator.paginate_queryset(posts, request)
    serializer = PostSerializer(paginated_posts, many=True)
    return paginator.get_paginated_response(serializer.data)

# -----------------------------
# Like/Unlike APIs
# -----------------------------
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        return Response({"detail": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)

    # Optionally, create a notification for post author
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )

    return Response({"detail": "Post liked"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({"detail": "Post unliked"}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response({"detail": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)
