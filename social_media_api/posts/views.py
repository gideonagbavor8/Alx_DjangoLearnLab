from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing posts with CRUD operations.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = PageNumberPagination  # Enable pagination
    filter_backends = [SearchFilter]         # Enable filtering
    search_fields = ['title', 'content']     # Allow filtering posts by title or content

    def perform_create(self, serializer):
        """
        Automatically set the author of the post to the logged-in user.
        """
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing comments with CRUD operations.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """
        Automatically set the author of the comment to the logged-in user.
        """
        serializer.save(author=self.request.user)


from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination  # Enable pagination
    filter_backends = [SearchFilter]         # Enable filtering
    search_fields = ['title', 'content']     # Filter posts by title or content
