from django.urls import path

from .views import (
    ShopListAPIView,
    ShopDetailAPIView,
    ShopSearchAPIView,
    FeaturedCategoryListAPIView,
    ProductsByCategoryAPIView,
)

urlpatterns = [

    # =========================
    # SHOPS
    # =========================

    path(
        "shops/",
        ShopListAPIView.as_view(),
        name="shop-list",
    ),
    
    path(
    "shops/<int:pk>/",
    ShopDetailAPIView.as_view(),
    name="shop-detail",
),

    path(
        "shops/search/",
        ShopSearchAPIView.as_view(),
        name="shop-search",
    ),

    # =========================
    # FEATURED CATEGORIES
    # =========================

    path(
        "categories/",
        FeaturedCategoryListAPIView.as_view(),
        name="category-list",
    ),

    path(
        "categories/<slug:slug>/",
        ProductsByCategoryAPIView.as_view(),
        name="products-by-category",
    ),
]