from django.contrib import admin

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from ..models import PageText


@admin.register(PageText)
class PageTextAdmin(UnfoldModelAdmin):
    list_display = ('key', 'text', 'text')
    search_fields = ('key', 'text')
    list_filter = ('key',)
