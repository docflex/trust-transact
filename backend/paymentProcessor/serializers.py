import uuid
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    order_id = serializers.CharField(required=True)
    order_amount = serializers.IntegerField(min_value=0, required=True)
    order_meta = serializers.CharField(default=lambda: str(uuid.uuid4()), read_only=True)

    class Meta:
        model = Order
        fields = (
            'order_id',
            'order_amount',
            'order_meta',
            'payment_url'
        )
    
    payment_url = serializers.SerializerMethodField(read_only=True)

    def get_payment_url(self, obj):
        # Replace this logic with actual payment URL generation
        payment_id = str(uuid.uuid4())  # Generate a sample payment ID
        return f"https://example.com/pay/{payment_id}"

class GetPaymentStatusSerializer(serializers.Serializer):
    order_id = serializers.CharField(required=True)
    status = serializers.CharField(read_only=True)