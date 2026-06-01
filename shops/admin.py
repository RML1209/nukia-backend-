from django.contrib import admin
from .models import Shop, Product


# =========================
# PRODUCT INLINE
# =========================

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1

    fields = (
        "product_name",
        "category",
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

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "product_name",
        "shop",
        "category",
        "product_image",
        "created_at",
    )

    search_fields = (
        "product_name",
        "keywords",
    )

    list_filter = (
        "category",
    )

    fields = (
        "shop",
        "product_name",
        "category",
        "keywords",
        "product_image",
    )