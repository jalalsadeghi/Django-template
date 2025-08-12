from django.contrib import admin
from .models import Article, ContactRequest

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_datetime", "is_online")
    list_filter = ("is_online", "publication_datetime")
    search_fields = ("title", "content", "author__username", "author__email")
    prepopulated_fields = {"slug": ("title",)}  # Prepopulate slug from title as requested

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")

    # Disallow add and change – only delete is possible, per brief
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False