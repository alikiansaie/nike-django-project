from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PU', 'Published'
        REJECTED = 'RJ', 'Rejected'

    # Details :
    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="user_posts")
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=300)
    size = models.CharField(max_length=10)
    types = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250)

    # Date :
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    date = models.DateField(default=timezone.now)
    # Situation :
    status = models.CharField(max_length=250, choices=Status.choices, default=Status.DRAFT)

    # manager :
    class PublishManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Post.Status.PUBLISHED)

    # Orderring & Searching :
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    objects = models.Manager()
    PublishManager = PublishManager()

    def __str__(self):
        return self.title
