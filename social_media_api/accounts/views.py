from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, LoginSerializer
# from posts.models import Post


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView
from .models import CustomUser
from .serializers import UserSerializer

class UserProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import CustomUser

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if user_to_follow != request.user:
            request.user.following.add(user_to_follow)
            return Response({'message': f'You are now following {user_to_follow.username}'}, status=200)
        return Response({'error': 'You cannot follow yourself'}, status=400)

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        if user_to_unfollow != request.user:
            request.user.following.remove(user_to_unfollow)
            return Response({'message': f'You have unfollowed {user_to_unfollow.username}'}, status=200)
        return Response({'error': 'You cannot unfollow yourself'}, status=400)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        followed_users = request.user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        feed_data = [{'title': post.title, 'content': post.content, 'author': post.author.username} for post in posts]
        return Response(feed_data, status=200)
