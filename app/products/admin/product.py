from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from unfold.admin import ModelAdmin as UnfoldModelAdmin, StackedInline
from unfold.decorators import display

from ..models import Product, ProductPhoto


class ProductPhotoInline(StackedInline):
    model = ProductPhoto
    extra = 1
    fields = ('photo', 'alt', 'order',)
    readonly_fields = ()
    ordering = ('order',)


@admin.register(Product)
class ProductAdmin(UnfoldModelAdmin):
    list_display = ('id', 'name', 'price', 'display_categories', 'display_tags', 'color', 'is_hidden', 'display_photo')
    list_display_links = ('id', 'name')
    list_editable = ('is_hidden',)
    list_filter = ('categories', 'tags', 'color')
    search_fields = ('name',)
    autocomplete_fields = ('categories', 'tags')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ProductPhotoInline]
    compressed_fields = True

    @display(description=_("Категории"))
    def display_categories(self, obj):
        return ", ".join([cat.name for cat in obj.categories.all()])

    @display(description=_("Теги"))
    def display_tags(self, obj):
        return ", ".join([cat.name for cat in obj.tags.all()])

    @display(description=_("Фото"))
    def display_photo(self, obj):
        if obj.banner_photo:
            return mark_safe(
                f'<img src="{obj.banner_photo.url}" height="120" width="120" '
                f'style="border-radius: 10%;" />')
        return '-'