# models.py
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs')
    blog_type = models.CharField(max_length=100)
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField()
    status = models.CharField(max_length=100)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title
