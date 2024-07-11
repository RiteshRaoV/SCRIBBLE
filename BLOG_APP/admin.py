from django.contrib import admin
from .models import Blog
from AUTH.models import CustomUser
# Register your models here.
admin.site.register(Blog)
admin.site.register(CustomUser)