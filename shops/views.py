from django.db.models import Q

from rest_framework import generics

from .models import Shop

from .serializers import ShopSerializer


# =========================
# SHOP LIST API
# =========================

class ShopListAPIView(generics.ListAPIView):

    queryset = Shop.objects.all()

    serializer_class = ShopSerializer


# =========================
# SEARCH API
# =========================

class ShopSearchAPIView(generics.ListAPIView):

    serializer_class = ShopSerializer

    def get_queryset(self):

        query = self.request.GET.get('q')

        if query:

            return Shop.objects.filter(

                Q(name__icontains=query) |

                Q(location__icontains=query) |

                Q(products__product_name__icontains=query) |

                Q(products__keywords__icontains=query)

            ).distinct()

        return Shop.objects.none()