from django.contrib import admin

from .models import Shop, Product


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'location',
        'phone',
        'is_verified',
        'views_count',
        'created_at'
    )

    search_fields = (
        'name',
        'location'
    )

    list_filter = (
        'is_verified',
        'created_at'
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'product_name',
        'shop',
        'category',
        'created_at'
    )

    search_fields = (
        'product_name',
        'keywords'
    )

    list_filter = (
        'category',
    )