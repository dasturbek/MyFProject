from django.contrib import admin
from .models import PostModel, PostCommentsModel
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(PostModel)
admin.site.register(PostCommentsModel)