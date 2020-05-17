from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PostUpvoteApi(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            post.upvotes += 1
            post.save()
            return Response({"detail": "upvoted"})
        except Post.DoesNotExist:
            return Response({"detail": "Not found."}, 404)
