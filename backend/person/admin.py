import textwrap

from django.contrib import admin

from person.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "short_bio",
        "company",
        "job_title",
        "birth_date",
        "experience",
    )
    list_filter = (
        "company",
        "job_title",
    )

    def short_bio(self, obj: Person) -> str:
        """short Person.bio"""
        if obj.bio:
            return textwrap.wrap(obj.bio, 55)[0]
        return ''
        