from rest_framework import serializers
from . models import Order, OrderDetails

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields='__all__'

class OrderDetailsSerializer(serializers.ModelSerializer):
    
    order_detail=OrderSerializers()

    class Meta:
        model = OrderDetails
        fields =['order_id','amount','order_detail']        