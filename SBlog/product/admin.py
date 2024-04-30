from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'status')
    ordering = ('title', 'publish')
    list_filter = ('status', 'publish', 'author')
    search_fields = ('title', 'slug', 'description')
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['status']
    list_display_links = ['author']
