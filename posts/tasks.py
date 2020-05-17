from celery import task
from .models import Post


@task(name="reset_posts_upvotes")
def reset_posts_upvotes():
    Post.objects.all().update(upvotes=0)
    print("posts upvotes reset")
