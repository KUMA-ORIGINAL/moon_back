from django.contrib import admin
from unfold.admin import ModelAdmin as UnfoldModelAdmin

from ..models import Color


@admin.register(Color)
class ColorAdmin(UnfoldModelAdmin):
    list_display = ('id', 'name', 'hex_code')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'hex_code')
