from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    author = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.CharField(max_length=64)
    content = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comment by {self.author} on {self.post}"
