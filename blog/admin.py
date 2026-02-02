from django.contrib import admin
from .models import Post

# Register your models here.

#admin.site.register(Post)

#personnalisation de l'interface d'administration
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author', 'pusblish', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body')
    ordering = ('author', 'status', 'pusblish')
    list_filter = ('status', 'created_at', 'pusblish', 'author')
    