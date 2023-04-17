from rest_framework import viewsets
from . models import *
from .serializers import OrderDetailsSerializer, OrderSerializers

class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializers

class OrderDetailsViewSet(viewsets.ModelViewSet):
    serializer_class=OrderDetailsSerializer
    queryset=OrderDetails.objects.all()
      