from django.contrib import admin
from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'totalCost', 'createdAt', 'status']
    list_display_links = ['pk', 'user']
