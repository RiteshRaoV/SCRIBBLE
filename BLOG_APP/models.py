# models.py
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db import models


class Blog(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blogs'
    )
    blog_type = models.CharField(
        max_length=100,
        default='tech'
    )
    blog_title = models.CharField(
        max_length=200
    )
    blog_description = models.CharField(
        max_length=255,
        help_text="Brief description of the blog post."
    )
    blog_thumbnail = models.ImageField(
        upload_to="thumbnails/",
        blank=True,
        null=True,
        help_text="Thumbnail image for the blog post."
    )
    blog_content = models.TextField()
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='pending'
    )
    publish_date = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the blog post was created."
    )

    class Meta:
        ordering = ['-publish_date']  # Order by latest publish date first

    def __str__(self):
        return self.blog_title

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    profile_pic = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True,
        help_text="Profile picture of the user."
    )

    def __str__(self):
        return f"{self.user.username}'s profile"