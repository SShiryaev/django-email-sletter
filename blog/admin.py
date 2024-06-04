from django.contrib import admin

from blog.models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'preview', 'created_at', 'views_count',)
