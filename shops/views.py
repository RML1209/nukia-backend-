from django.db.models import Q

from rest_framework import generics

from .models import (
    Shop,
    Product,
    FeaturedCategory,
)

from .serializers import (
    ShopSerializer,
    ProductSerializer,
    FeaturedCategorySerializer,
)


# =========================
# SHOP LIST API
# =========================

class ShopListAPIView(generics.ListAPIView):

    queryset = Shop.objects.all().prefetch_related(
        "products",
        "products__featured_categories"
    )

    serializer_class = ShopSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


# =========================
# SEARCH API
# =========================

class ShopSearchAPIView(generics.ListAPIView):

    serializer_class = ShopSerializer

    def get_queryset(self):

        query = self.request.GET.get("q")

        if query:

            return Shop.objects.filter(

                Q(name__icontains=query) |

                Q(location__icontains=query) |

                Q(products__product_name__icontains=query) |

                Q(products__keywords__icontains=query)

            ).prefetch_related(
                "products",
                "products__featured_categories"
            ).distinct()

        return Shop.objects.none()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


# =========================
# FEATURED CATEGORY LIST API
# =========================

class FeaturedCategoryListAPIView(
    generics.ListAPIView
):

    queryset = FeaturedCategory.objects.all()

    serializer_class = (
        FeaturedCategorySerializer
    )


# =========================
# PRODUCTS BY CATEGORY API
# =========================

class ProductsByCategoryAPIView(
    generics.ListAPIView
):

    serializer_class = ProductSerializer

    def get_queryset(self):

        slug = self.kwargs.get("slug")

        return Product.objects.filter(
            featured_categories__slug=slug
        ).select_related(
            "shop"
        ).prefetch_related(
            "featured_categories"
        )

    def get_serializer_context(self):

        context = super().get_serializer_context()

        context["request"] = self.request

        return context