import textwrap
from django.contrib import admin

from article.models import Article, ArticleAdditionalInformation, ArticleTag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "short_description", "author")
    list_filter = ("author",)

    filter_horizontal = ('tags',)

    def short_description(self, obj: Article):
        """short Article.description"""
        return textwrap.wrap(obj.description, 55)


@admin.register(ArticleAdditionalInformation)
class ArticleFullInfo(admin.ModelAdmin):
    list_display = ("full_description", "image", "is_approved_by_admin")


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('name', "short_description", 'created_at')
    