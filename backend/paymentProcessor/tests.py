from .models import Order
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
import uuid

class OrderTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.data = {
            "order_id": str(uuid.uuid4()),
            "order_amount": 100,
            # order_meta will be automatically generated
        }
        self.url = "/createPayment/"

    def test_create_payment(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().order_id, self.data['order_id'])

    def test_create_payment_without_order_id(self):
        data = self.data.copy()
        data.pop("order_id")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_payment_without_order_amount(self):
        data = self.data.copy()
        data.pop("order_amount")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_payment_with_negative_order_amount(self):
        data = self.data.copy()
        data["order_amount"] = -50
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # ... other test methods ...
