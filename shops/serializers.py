from rest_framework import serializers

from .models import Shop, Product


# =========================
# PRODUCT SERIALIZER
# =========================

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


# =========================
# SHOP SERIALIZER
# =========================

class ShopSerializer(serializers.ModelSerializer):

    products = ProductSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Shop

        fields = [
            'id',
            'name',
            'location',
            'phone',
            'instagram',
            'description',
            'profile_image',
            'map_link',
            'is_verified',
            'views_count',
            'products',
        ]