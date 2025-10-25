from django.db import migrations
import random


def assign_roles_to_persons(apps, schema_editor):
    Person = apps.get_model('person', 'Person')
    Role = apps.get_model('person', 'Role')
    UserRole = apps.get_model('person', 'UserRole')
    
    persons = list(Person.objects.all())
    roles = list(Role.objects.all())
    
    if not persons or not roles:
        print("No persons or roles found. Skipping role assignment.")
        return
    
    status_choices = ['active', 'active', 'active', 'inactive', 'pending']
    
    for person in persons:
        num_roles = random.randint(2, 4)
        selected_roles = random.sample(roles, min(num_roles, len(roles)))
        
        for role in selected_roles:
            status = random.choice(status_choices)
            UserRole.objects.create(
                person=person,
                role=role,
                status=status
            )
    
    print(f"Successfully assigned roles to {len(persons)} persons.")


def reverse_func(apps, schema_editor):
    UserRole = apps.get_model('person', 'UserRole')
    
    UserRole.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_role_data'),
    ]

    operations = [
        migrations.RunPython(assign_roles_to_persons, reverse_func),
    ]
