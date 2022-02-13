from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Post(models.Model):
    STATUS_CHOICE = (
        ("published", "PUBLISHED"),
        ("draft", "DRAFT"),
    )
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default="draft")

    object = models.Manager()
    published = PublishManager()

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title + "--" + self.author.username
