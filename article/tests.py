from rest_framework.test import APITestCase
from rest_framework import status
from article.models import ArticleTag

# Create your tests here.
class TestArticleTag(APITestCase):

    def setUp(self):
        self.article_tag = ArticleTag.objects.create(
            name="test tag", short_description="test tag description"
        )
        self.url = '/api/v1/article-tag/'

    def test_create_article_tag(self):
        create_data = {
            'name':'create test tag',
            'short_description': 'short_description test tag'
        }
        response = self.client.post(self.url, create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ArticleTag.objects.count(), 2)
