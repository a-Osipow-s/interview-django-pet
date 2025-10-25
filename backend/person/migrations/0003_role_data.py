from django.db import migrations


def create_sample_roles(apps, schema_editor):
    Role = apps.get_model('person', 'Role')
    
    roles_data = [
        {
            "role_name": "Administrator",
            "role_description": "Full system access with all permissions. Can manage users, roles, settings, and all system configurations. Has complete control over the platform."
        },
        {
            "role_name": "Editor",
            "role_description": "Can create, edit, and publish content. Has access to content management features including articles, reviews, and media. Can moderate user-generated content."
        },
        {
            "role_name": "Reviewer",
            "role_description": "Can review and rate articles. Has permission to submit reviews, provide ratings, and offer feedback on submitted content. Cannot publish or delete content."
        },
        {
            "role_name": "Author",
            "role_description": "Can create and submit articles for review. Has access to writing tools and draft management. Can edit own content but cannot publish without approval."
        },
        {
            "role_name": "Moderator",
            "role_description": "Can moderate user content, comments, and reviews. Has permission to flag inappropriate content, manage user reports, and enforce community guidelines."
        },
        {
            "role_name": "Viewer",
            "role_description": "Read-only access to published content. Can view articles, reviews, and public information. Cannot create, edit, or delete any content."
        },
        {
            "role_name": "Contributor",
            "role_description": "Can submit content suggestions and participate in discussions. Has limited editing capabilities and can collaborate on draft content with authors."
        },
        {
            "role_name": "Manager",
            "role_description": "Can manage teams and workflows. Has access to analytics, reports, and team performance metrics. Can assign tasks and oversee project progress."
        },
        {
            "role_name": "Analyst",
            "role_description": "Can access analytics and reporting tools. Has permission to view system metrics, user engagement data, and generate performance reports. Read-only access to data."
        },
        {
            "role_name": "Guest",
            "role_description": "Limited temporary access to specific features. Can view public content and participate in limited interactions. Requires upgrade for full platform access."
        },
    ]
    
    for role_data in roles_data:
        Role.objects.create(
            role_name=role_data['role_name'],
            role_description=role_data['role_description']
        )


def reverse_func(apps, schema_editor):
    Role = apps.get_model('person', 'Role')
    
    role_names = [
        "Administrator", "Editor", "Reviewer", "Author", "Moderator",
        "Viewer", "Contributor", "Manager", "Analyst", "Guest"
    ]
    
    Role.objects.filter(role_name__in=role_names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_person_data'),
    ]

    operations = [
        migrations.RunPython(create_sample_roles, reverse_func),
    ]