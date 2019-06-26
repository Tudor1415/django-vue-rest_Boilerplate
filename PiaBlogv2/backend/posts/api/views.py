from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from ..models import Post
from .serializers import PostDetailSerializer, PostListSerializer, PostCreateUpdateSerializer

class PostListApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class  = PostListSerializer


    def get_queryset(self):
        return super().get_queryset()

class PostDetailApiView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class  = PostDetailSerializer


    def get_queryset(self):
        return super().get_queryset()

class PostUpdateApiView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class  = PostDetailSerializer


    def get_queryset(self):
        return super().get_queryset()

class PostDeleteApiView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class  = PostDetailSerializer


    def get_queryset(self):
        return super().get_queryset()

class PostCreateApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class  = PostCreateUpdateSerializer


    def get_queryset(self):
        return super().get_queryset()