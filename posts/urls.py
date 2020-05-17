from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import CommentViewSet, PostViewSet, PostUpvoteApi
from django.urls import path

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)

urlpatterns = router.urls

urlpatterns.append(
    path("posts/upvote/<int:post_id>/", PostUpvoteApi.as_view())
)
