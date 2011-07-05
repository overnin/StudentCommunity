from community.models import GoogleGroup, Post #@UnresolvedImport
from django.contrib import admin


class PostInline(admin.TabularInline):
    model = Post
    extra = 1

class GoogleGroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [PostInline]

admin.site.register(GoogleGroup, GoogleGroupAdmin)