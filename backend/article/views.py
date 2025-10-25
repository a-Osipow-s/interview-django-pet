from django.core.mail import send_mail
from django.conf import settings

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response

from article.models import Article, ArticleAdditionalInformation, ArticleTag, ArticleReview
from person.models import Person


# serializers
class ArticleAdditionalInformationSerializer(ModelSerializer):
    class Meta:
        model = ArticleAdditionalInformation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        depth = kwargs.pop('depth', None)
        super().__init__(*args, **kwargs)
        
        if depth is not None:
            self.Meta.depth = min(depth, 9)


class ArticleReviewSerializer(ModelSerializer):
    class Meta:
        model = ArticleReview
        fields = '__all__'
        depth = 9


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        depth = kwargs.pop('depth', None)
        super().__init__(*args, **kwargs)
        
        if depth is not None:
            self.Meta.depth = min(depth, 9)


class ArticleTagSerializer(ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = '__all__'


# views
def get_article_reviewers():
    persons = Person.objects.all()
    result_persons = []
    for person in persons:
        roles = [ur.role for ur in person.user_roles.all() if ur.status == 'active']
        for role in roles:
            if role.role_name == 'Reviewer':
                result_persons.append(person)
    return person


class ArticleTagViewSet(ModelViewSet):
    queryset = ArticleTag.objects.all().order_by('-created_at')
    serializer_class = ArticleTagSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_serializer(self, *args, **kwargs):
        depth: int = self.request.query_params.get('depth')
        if depth:
            kwargs['depth'] = int(depth)
        return super().get_serializer(*args, **kwargs)

    def perform_create(self, serializer):
        article: Article = serializer.save()
        author: Person = article.author
        if author and author.email:
            send_mail(
                subject=f"New article published: {article.title}",
                message=f"Hi {author.name}, your article '{article.title}' was successfully created!",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[author.email],
                fail_silently=False,
            )
        for reviewer in get_article_reviewers():
            send_mail(
                subject=f"New article published: {article.title}",
                message=f"Hi {reviewer.name}, new article '{article.title}' was successfully created!",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[reviewer.email],
                fail_silently=False,
            )
    
    def perform_update(self, serializer):
        article: Article = serializer.save()
        author: Person = article.author
        article.additional_info.refresh_from_db()
        is_approved: bool = article.additional_info.is_approved_by_admin

        if is_approved:
            if author and author.email:
                send_mail(
                    subject=f"Your article approved: {article.title}",
                    message=f"Hi {author.name}, your article '{article.title}' was approved!",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[author.email],
                    fail_silently=False,
                )
            for reviewer in get_article_reviewers():
                send_mail(
                    subject=f"New article approved: {article.title}",
                    message=f"Hi {reviewer.name}, new article '{article.title}' was approved!",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[reviewer.email],
                    fail_silently=False,
                )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        result_items = []
        for article in serializer.data:
            reviews: list[ArticleReview] = ArticleReview.objects.filter(article__id=article['id'])
            sum_of_rating: int = sum([review.overall_rating for review in reviews])
            avg: float = sum_of_rating / len(reviews) if sum_of_rating else 0
            result_items.append(
                {
                    'article': article,
                    'avg_rating': avg, 
                    'reviewers': [{
                        'id': review.reviewer.user.id,
                        'first_name': review.reviewer.user.first_name,
                        'last_name': review.reviewer.user.last_name,
                        'email': review.reviewer.user.email,
                    } for review in reviews],
                }
            )
        return Response(result_items, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)