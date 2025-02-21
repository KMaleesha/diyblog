from django.contrib import admin
from .models import Genre, Language, Blogger, Blog, Comment

admin.site.register(Genre)
admin.site.register(Language)

class BloggerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    
admin.site.register(Blogger, BloggerAdmin)
admin.site.register(Comment)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date', 'blogger')