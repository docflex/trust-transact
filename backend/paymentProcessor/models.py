from django.db import models
from utils.model_abstracts import BaseOrder

class Order(BaseOrder):
    order_id = models.CharField(max_length=100, unique=True)
    order_amount = models.PositiveIntegerField()

    def __str__(self):
        return f'Order ID: {self.order_id}'
