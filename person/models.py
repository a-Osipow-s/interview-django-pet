from django import dispatch
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save


class Person(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True, default="")
    company = models.CharField(max_length=100, null=True, blank=False)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    experience = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=False)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return str(self.user)


@dispatch.receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)
