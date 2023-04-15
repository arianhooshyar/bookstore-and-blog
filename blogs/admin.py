from django.contrib import admin
from .models import Blog, Comment


# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'update_at', 'active', ]
    ordering = ['update_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'blog', 'create_at', ]
