from django.contrib import admin

from .models import (
    Shop,
    Product,
    FeaturedCategory
)


# =========================
# FEATURED CATEGORY ADMIN
# =========================

@admin.register(FeaturedCategory)
class FeaturedCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
        "created_at",
    )

    search_fields = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


# =========================
# PRODUCT INLINE
# =========================

class ProductInline(admin.TabularInline):

    model = Product

    extra = 1

    fields = (
        "product_name",
        "category",
        "product_price",
        "keywords",
        "product_image",
    )


# =========================
# SHOP ADMIN
# =========================

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "location",
        "phone",
        "is_verified",
        "views_count",
        "created_at",
    )

    search_fields = (
        "name",
        "location",
    )

    list_filter = (
        "is_verified",
        "created_at",
    )

    inlines = [ProductInline]


# =========================
# PRODUCT ADMIN
# =========================
from django.utils.html import format_html


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "product_name",
        "shop",
        "category",
        "product_price",
        "image_preview",
        "display_categories",
        "created_at",
    )

    search_fields = (
        "product_name",
        "keywords",
        "shop__name",
    )

    list_filter = (
        "category",
        "featured_categories",
        "created_at",
    )

    filter_horizontal = (
        "featured_categories",
    )

    fields = (
        "shop",
        "product_name",
        "category",
        "product_price",
        "keywords",
        "product_image",
        "featured_categories",
    )

    def image_preview(self, obj):
        if obj.product_image:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:8px;" />',
                obj.product_image.url
            )
        return "-"

    image_preview.short_description = "Image"

    def display_categories(self, obj):
        return ", ".join(
            category.name
            for category in obj.featured_categories.all()
        )

    display_categories.short_description = "Featured Categories"