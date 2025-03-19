from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at' )

    def get_deleted_at(self, obj):
        return obj.deleted_at if obj.deleted_at else "Active"
    get_deleted_at.short_description = 'Deleted At'

    def get_deleted_by(self, obj):
        return obj.deleted_by if obj.deleted_by else "Not Deleted"
    get_deleted_by.short_description = 'Deleted By'

admin.site.register(BlogPost, BlogPostAdmin)
