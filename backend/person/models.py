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


class Role(models.Model):
    role_name = models.CharField(max_length=100, unique=True)
    role_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("role_name",)

    def __str__(self):
        return self.role_name


class UserRole(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
    ]
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='user_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='user_roles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        unique_together = ('person', 'role')

    def __str__(self):
        return f"{self.person} - {self.role} ({self.status})"


@dispatch.receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)
