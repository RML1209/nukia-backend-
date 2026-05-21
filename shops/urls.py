from django.urls import path

from .views import (
    ShopListAPIView,
    ShopSearchAPIView
)


urlpatterns = [

    path(
        'shops/',
        ShopListAPIView.as_view(),
        name='shop-list'
    ),

    path(
        'shops/search/',
        ShopSearchAPIView.as_view(),
        name='shop-search'
    ),

]