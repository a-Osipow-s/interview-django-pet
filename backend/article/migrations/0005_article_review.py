from django.db import migrations
from django.utils import timezone
import random
from datetime import timedelta


def create_article_reviews(apps, schema_editor):
    Article = apps.get_model('article', 'Article')
    ArticleReview = apps.get_model('article', 'ArticleReview')
    Person = apps.get_model('person', 'Person')
    Role = apps.get_model('person', 'Role')
    
    articles = list(Article.objects.all())
    
    if not articles:
        print("No articles found. Skipping review creation.")
        return
    
    try:
        reviewer_role = Role.objects.get(role_name='Reviewer')
        active_reviewers = Person.objects.filter(
            user_roles__role=reviewer_role,
            user_roles__status='active'
        ).distinct()
        reviewers_list = list(active_reviewers)
    except Role.DoesNotExist:
        print("Reviewer role not found. Skipping review creation.")
        return
    
    if not reviewers_list:
        print("No active reviewers found. Skipping review creation.")
        return
    
    num_articles_to_review = int(len(articles) * 0.9)
    articles_to_review = random.sample(articles, num_articles_to_review)
    
    positive_titles = [
        "Excellent Technical Content",
        "Highly Informative Article",
        "Well-Written and Clear",
        "Outstanding Tutorial",
        "Comprehensive Guide",
        "Great Practical Examples",
        "Very Helpful Resource",
        "Professional Quality Content",
        "Impressive Depth of Coverage",
        "Valuable Learning Material"
    ]
    
    neutral_titles = [
        "Good Article with Minor Issues",
        "Solid Content, Needs Polish",
        "Decent Coverage of Topic",
        "Adequate Technical Explanation",
        "Fair Treatment of Subject",
        "Good Start, Could Be Better",
        "Reasonable Overview",
        "Acceptable Quality Content"
    ]
    
    critical_titles = [
        "Needs Significant Improvement",
        "Lacking Technical Depth",
        "Requires Major Revision",
        "Incomplete Coverage",
        "Could Use More Detail",
        "Missing Key Information"
    ]
    
    strengths_templates = [
        "Clear explanations with practical examples. Well-structured content that flows logically. Good use of code snippets.",
        "Comprehensive coverage of the topic. Excellent balance between theory and practice. Helpful diagrams and illustrations.",
        "Easy to follow for beginners. Step-by-step approach is very helpful. Good introduction to the subject matter.",
        "Strong technical accuracy. Well-researched content with credible references. Up-to-date information.",
        "Engaging writing style. Maintains reader interest throughout. Good use of real-world scenarios.",
        "Thorough explanations of complex concepts. Good depth of technical detail. Professional presentation.",
        "Practical code examples that work. Clear documentation. Helpful troubleshooting tips included.",
        "Well-organized structure. Easy navigation. Good summary and conclusions.",
        "Addresses common pitfalls. Includes best practices. Helpful warnings about potential issues.",
        "Modern approach to the topic. Current with latest technologies. Relevant to industry standards."
    ]
    
    weaknesses_templates = [
        "Could benefit from more detailed examples. Some sections feel rushed.",
        "Minor typos and grammatical errors present. Needs proofreading.",
        "Would benefit from additional diagrams or visual aids.",
        "Some code examples could be more complete. Missing error handling in places.",
        "Could expand on certain advanced topics. Feels slightly superficial in areas.",
        "References could be more current. Some information may be slightly outdated.",
        "Could use more real-world use cases. Examples are somewhat basic.",
        "Navigation between sections could be smoother. Some repetition in content.",
        "Assumes prior knowledge in some areas. Could benefit from more introductory material.",
        "Could include more performance considerations. Missing optimization tips."
    ]
    
    suggestions_templates = [
        "Consider adding a troubleshooting section. Include more edge cases. Expand the conclusion with next steps.",
        "Add links to additional resources. Include a glossary of terms. Consider video demonstrations.",
        "Provide downloadable code samples. Add interactive examples. Include unit tests.",
        "Expand advanced topics section. Add comparison with alternative approaches. Include benchmarks.",
        "Add more visual content. Include architecture diagrams. Consider infographics for key concepts.",
        "Update references to latest versions. Add migration guides. Include compatibility notes.",
        "Provide more context for beginners. Add prerequisite section. Include learning path recommendations.",
        "Add FAQ section. Include common errors and solutions. Provide community resources.",
        "Consider splitting into multiple parts. Add table of contents. Include quick reference guide.",
        "Add real-world case studies. Include industry examples. Provide production deployment guidance."
    ]
    
    status_choices = ['pending', 'approved', 'approved', 'approved', 'rejected', 'revision_required']
    
    created_count = 0
    
    for article in articles_to_review:
        num_reviews = random.randint(1, 3)
        
        selected_reviewers = random.sample(
            reviewers_list, 
            min(num_reviews, len(reviewers_list))
        )
        
        for reviewer in selected_reviewers:
            if ArticleReview.objects.filter(article=article, reviewer=reviewer).exists():
                continue
            
            overall_rating = random.randint(2, 5)
            
            content_quality_rating = max(1, min(5, overall_rating + random.randint(-1, 1)))
            originality_rating = max(1, min(5, overall_rating + random.randint(-1, 1)))
            technical_accuracy_rating = max(1, min(5, overall_rating + random.randint(-1, 1)))
            clarity_rating = max(1, min(5, overall_rating + random.randint(-1, 1)))
            confidence_level = random.randint(3, 5)
            
            if overall_rating >= 4:
                review_title = random.choice(positive_titles)
            elif overall_rating == 3:
                review_title = random.choice(neutral_titles)
            else:
                review_title = random.choice(critical_titles)
            
            review_summary = f"This article provides {'excellent' if overall_rating >= 4 else 'adequate' if overall_rating == 3 else 'limited'} coverage of {article.title.lower()}. "
            review_summary += random.choice([
                "The content is well-researched and presents information clearly.",
                "The technical explanations are generally sound with some minor gaps.",
                "The tutorial approach makes complex topics accessible.",
                "The practical examples enhance understanding significantly.",
                "The structure helps readers follow the material effectively."
            ])
            
            strengths = random.choice(strengths_templates)
            weaknesses = random.choice(weaknesses_templates) if overall_rating < 5 else ""
            suggestions = random.choice(suggestions_templates) if overall_rating < 5 else ""
            
            status = random.choice(status_choices)
            is_verified_reviewer = random.choice([True, True, True, False])
            is_public = random.choice([True, True, True, False])
            is_anonymous = random.choice([False, False, False, True])
            recommend_for_publication = overall_rating >= 3
            
            days_ago = random.randint(1, 60)
            reviewed_at = timezone.now() - timedelta(days=days_ago)
            
            ArticleReview.objects.create(
                article=article,
                reviewer=reviewer,
                overall_rating=overall_rating,
                content_quality_rating=content_quality_rating,
                originality_rating=originality_rating,
                technical_accuracy_rating=technical_accuracy_rating,
                clarity_rating=clarity_rating,
                review_title=review_title,
                review_summary=review_summary,
                strengths=strengths,
                weaknesses=weaknesses,
                suggestions=suggestions,
                status=status,
                is_verified_reviewer=is_verified_reviewer,
                is_public=is_public,
                is_anonymous=is_anonymous,
                recommend_for_publication=recommend_for_publication,
                confidence_level=confidence_level,
                reviewed_at=reviewed_at
            )
            
            created_count += 1
    
    print(f"Successfully created {created_count} article reviews for {len(articles_to_review)} articles.")
    print(f"Reviews created by {len(reviewers_list)} active reviewers.")


def reverse_func(apps, schema_editor):
    ArticleReview = apps.get_model('article', 'ArticleReview')
    
    ArticleReview.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_full_info'),
    ]

    operations = [
        migrations.RunPython(create_article_reviews, reverse_func),
    ]