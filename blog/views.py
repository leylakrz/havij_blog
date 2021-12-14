# Create your views here.
from rest_framework import generics, permissions

from blog.models import Post
from blog.permission import IsOwnerOrAdmin
from blog.serializers import PostSerializer


class PostsDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostsUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
