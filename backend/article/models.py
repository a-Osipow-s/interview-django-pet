from django.db import models
from person.models import Person

from .utils import article_image_path


class ArticleAdditionalInformation(models.Model):
    full_description = models.TextField(null=False, blank=True)
    is_approved_by_admin = models.BooleanField(null=False, blank=False, default=False)
    image = models.ImageField(upload_to=article_image_path, null=True, blank=True)

    def __str__(self):
        return self.full_description[:50]

    class Meta:
        ordering = ("id",)


class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=True)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    tags = models.ManyToManyField('ArticleTag', blank=True, related_name="tags")
    additional_info = models.OneToOneField(ArticleAdditionalInformation, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

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


class ArticleReview(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('revision_required', 'Revision Required'),
    ]
    
    # Core fields
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='article_reviews')
    
    # Rating fields
    overall_rating = models.IntegerField(choices=RATING_CHOICES)
    content_quality_rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    originality_rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    technical_accuracy_rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    clarity_rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    
    # Review content
    review_title = models.CharField(max_length=200, blank=True)
    review_summary = models.TextField()
    strengths = models.TextField(blank=True)
    weaknesses = models.TextField(blank=True)
    suggestions = models.TextField(blank=True)
    
    # Status and metadata
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_verified_reviewer = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    is_anonymous = models.BooleanField(default=False)
    
    # Recommendations
    recommend_for_publication = models.BooleanField(default=False)
    confidence_level = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True, 
                                          help_text="Reviewer's confidence in their assessment")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ("-created_at",)
        unique_together = ('article', 'reviewer')

    def __str__(self):
        return f"Review of '{self.article.title}' by {self.reviewer}"
