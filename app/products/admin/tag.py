from django.contrib import admin
from unfold.admin import ModelAdmin as UnfoldModelAdmin

from ..models import Tag


@admin.register(Tag)
class TagAdmin(UnfoldModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
