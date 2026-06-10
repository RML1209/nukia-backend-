from django.db import models


# =========================
# SHOP MODEL
# =========================

class Shop(models.Model):

    name = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    phone = models.CharField(max_length=20)

    instagram = models.URLField(blank=True)

    description = models.TextField()

    profile_image = models.ImageField(
        upload_to="shops/",
        blank=True,
        null=True
    )

    map_link = models.URLField(blank=True)

    is_verified = models.BooleanField(default=False)

    views_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# FEATURED CATEGORY MODEL
# =========================

class FeaturedCategory(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


# =========================
# PRODUCT MODEL
# =========================

class Product(models.Model):

    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name="products"
    )

    product_name = models.CharField(
        max_length=200
    )

    category = models.CharField(
        max_length=100,
        blank=True
    )

    # PRODUCT IMAGE
    product_image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    # PRODUCT PRICE
    product_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )

    # FEATURED CATEGORIES
    featured_categories = models.ManyToManyField(
        FeaturedCategory,
        blank=True,
        related_name="products"
    )

    keywords = models.TextField(
        help_text="Separate keywords with commas",
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.product_name