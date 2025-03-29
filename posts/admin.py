from django.contrib import admin
from .models import Post, PostMedia, Comment, Report

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content_preview', 'place', 'route', 'like_count', 'is_public', 'created_at')
    list_filter = ('is_public', 'created_at', 'author')
    search_fields = ('author__username', 'content', 'hashtags')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content'

@admin.register(PostMedia)
class PostMediaAdmin(admin.ModelAdmin):
    list_display = ('post', 'media_type', 'caption', 'order', 'created_at')
    list_filter = ('media_type',)
    search_fields = ('post__content', 'caption')
    ordering = ('post', 'order')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'content_preview', 'like_count', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('author__username', 'post__content', 'content')
    ordering = ('-created_at',)

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content'

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'report_type', 'status', 'created_at')
    list_filter = ('report_type', 'status')
    search_fields = ('reporter__username', 'description')
    ordering = ('-created_at',)
