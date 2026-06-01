from rest_framework import serializers

from .models import Shop, Product


# =========================
# PRODUCT SERIALIZER
# =========================

class ProductSerializer(serializers.ModelSerializer):

    product_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "shop",
            "product_name",
            "category",
            "keywords",
            "product_image",
            "created_at",
        ]

    def get_product_image(self, obj):
        request = self.context.get("request")

        if obj.product_image:
            if request:
                return request.build_absolute_uri(
                    obj.product_image.url
                )
            return obj.product_image.url

        return None


# =========================
# SHOP SERIALIZER
# =========================

class ShopSerializer(serializers.ModelSerializer):

    profile_image = serializers.SerializerMethodField()

    products = serializers.SerializerMethodField()

    class Meta:
        model = Shop

        fields = [
            "id",
            "name",
            "location",
            "phone",
            "instagram",
            "description",
            "profile_image",
            "map_link",
            "is_verified",
            "views_count",
            "products",
        ]

    def get_profile_image(self, obj):
        request = self.context.get("request")

        if obj.profile_image:
            if request:
                return request.build_absolute_uri(
                    obj.profile_image.url
                )
            return obj.profile_image.url

        return None

    def get_products(self, obj):
        serializer = ProductSerializer(
            obj.products.all(),
            many=True,
            context=self.context
        )

        return serializer.data