from django.contrib import admin
from .models import Blog, UserProfile
from AUTH.models import CustomUser
# Register your models here.
admin.site.register(Blog)
admin.site.register(UserProfile)
admin.site.register(CustomUser)