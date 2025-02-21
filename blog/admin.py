from django.contrib import admin
from .models import Blogger, Blog, Comment


class BloggerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    
admin.site.register(Blogger, BloggerAdmin)
# admin.site.register(Comment)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date', 'blogger')
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter', 'blog', 'created_at')
    list_filter = ('created_at', 'commenter')