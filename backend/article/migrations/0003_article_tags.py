from django.db import migrations

def create_article_tags(apps, schema_editor):
    ArticleTag = apps.get_model('article', 'ArticleTag')
    
    tags_data = [
        {
            "name": "Python",
            "short_description": "Articles about Python programming language, frameworks, and best practices"
        },
        {
            "name": "JavaScript",
            "short_description": "Content related to JavaScript, TypeScript, and modern JS frameworks"
        },
        {
            "name": "Web Development",
            "short_description": "Full-stack web development, frontend, backend, and web technologies"
        },
        {
            "name": "Machine Learning",
            "short_description": "ML algorithms, neural networks, and artificial intelligence topics"
        },
        {
            "name": "DevOps",
            "short_description": "CI/CD, containerization, cloud infrastructure, and deployment practices"
        },
        {
            "name": "Data Science",
            "short_description": "Data analysis, visualization, statistics, and data-driven insights"
        },
        {
            "name": "Mobile Development",
            "short_description": "iOS, Android, and cross-platform mobile application development"
        },
        {
            "name": "Cybersecurity",
            "short_description": "Security best practices, ethical hacking, and threat protection"
        },
        {
            "name": "Cloud Computing",
            "short_description": "AWS, Azure, GCP, and cloud-native application development"
        },
        {
            "name": "Database",
            "short_description": "SQL, NoSQL, database design, optimization, and management"
        },
        {
            "name": "UI/UX Design",
            "short_description": "User interface design, user experience, and design thinking"
        },
        {
            "name": "API Development",
            "short_description": "REST, GraphQL, API design patterns, and integration techniques"
        },
        {
            "name": "Blockchain",
            "short_description": "Cryptocurrency, smart contracts, and decentralized applications"
        },
        {
            "name": "Agile",
            "short_description": "Scrum, Kanban, agile methodologies, and project management"
        },
        {
            "name": "Testing",
            "short_description": "Unit testing, integration testing, TDD, and quality assurance"
        },
        {
            "name": "Performance",
            "short_description": "Code optimization, scaling, and application performance tuning"
        },
        {
            "name": "Open Source",
            "short_description": "Contributing to open source projects and community collaboration"
        },
        {
            "name": "Career",
            "short_description": "Professional development, interviews, and career advancement tips"
        },
        {
            "name": "Architecture",
            "short_description": "Software architecture, design patterns, and system design"
        },
        {
            "name": "Tutorial",
            "short_description": "Step-by-step guides, how-tos, and educational content"
        },
    ]
    
    for tag_data in tags_data:
        ArticleTag.objects.create(
            name=tag_data['name'],
            short_description=tag_data['short_description']
        )
    
    print(f"Successfully created {len(tags_data)} article tags.")


def reverse_func(apps, schema_editor):
    ArticleTag = apps.get_model('article', 'ArticleTag')
    
    tag_names = [
        "Python", "JavaScript", "Web Development", "Machine Learning", "DevOps",
        "Data Science", "Mobile Development", "Cybersecurity", "Cloud Computing",
        "Database", "UI/UX Design", "API Development", "Blockchain", "Agile",
        "Testing", "Performance", "Open Source", "Career", "Architecture", "Tutorial"
    ]
    
    ArticleTag.objects.filter(name__in=tag_names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_additional_info'),
    ]

    operations = [
        migrations.RunPython(create_article_tags, reverse_func),
    ]
