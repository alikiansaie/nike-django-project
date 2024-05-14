from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels


# Create your models here.


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PU', 'Published'
        REJECTED = 'RJ', 'Rejected'

    # Details :
    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="user_posts", verbose_name="نویسنده")
    title = models.CharField(max_length=250, verbose_name="موضوع")
    description = models.TextField(max_length=300)
    size = models.CharField(max_length=10)
    types = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, verbose_name="اسلاگ")

    # Date :
    publish = jmodels.jDateTimeField(default=timezone.now)
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)
    date = jmodels.jDateField(default=timezone.now)
    # Situation :
    status = models.CharField(max_length=250, choices=Status.choices, default=Status.DRAFT, verbose_name="وضعیت")

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
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    objects = jmodels.jManager()
    PublishManager = PublishManager()

    def __str__(self):
        return self.title
