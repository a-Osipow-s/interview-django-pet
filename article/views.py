from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
# Create your views here.
from article.models import ArticleTag

class ArticleTagSerializer(ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = ['id', 'name', 'short_description', 'created_at']


class ArticleTagViewSet(ModelViewSet):
    queryset = ArticleTag.objects.all().order_by('-created_at')
    serializer_class = ArticleTagSerializer

