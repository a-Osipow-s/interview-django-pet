from django.db import models
from person.models import Person

from .utils import article_image_path


class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=True)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    tags = models.ManyToManyField('ArticleTag', blank=True, related_name="tags")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("id",)


class ArticleAdditionalInformation(models.Model):
    full_description = models.TextField(null=False, blank=True)
    is_approved_by_admin = models.BooleanField(null=False, blank=False, default=False)
    image = models.ImageField(upload_to=article_image_path, null=True, blank=True)

    def __str__(self):
        return self.full_description[:50]

    class Meta:
        ordering = ("id",)


class ArticleTag(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    short_description = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id",)
