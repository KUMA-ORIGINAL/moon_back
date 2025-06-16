from django.contrib import admin

from unfold.admin import ModelAdmin as UnfoldModelAdmin, TabularInline
from unfold.contrib.filters.admin import RangeDateTimeFilter

from ..models import Order, OrderItem


class OrderItemInline(TabularInline):
    model = OrderItem
    extra = 1
    fields = ('product', 'quantity', 'price',)


@admin.register(Order)
class OrderAdmin(UnfoldModelAdmin):
    list_filter_submit = True
    list_display = ['id', 'first_name', 'last_name', 'total_price', 'status', 'created_at']
    list_display_links = ['id', 'first_name', 'last_name',]
    list_filter = ['status', ('created_at', RangeDateTimeFilter)]
    search_fields = ['first_name', 'last_name', 'id']
    readonly_fields = ['created_at', 'updated_at']
    inlines = (OrderItemInline,)
