from django.contrib import admin

from blog.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'preview_image', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'content', )
    ordering = ('-created_at', )