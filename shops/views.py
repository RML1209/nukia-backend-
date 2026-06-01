from django.db.models import Q

from rest_framework import generics

from .models import Shop
from .serializers import ShopSerializer


# =========================
# SHOP LIST API
# =========================

class ShopListAPIView(generics.ListAPIView):

    queryset = Shop.objects.all().prefetch_related("products")

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
            ).prefetch_related("products").distinct()

        return Shop.objects.none()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context