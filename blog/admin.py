from django.contrib import admin

# Register your models here.
from blog.models import Post, Tag

admin.site.register(Tag)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
