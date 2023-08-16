import uuid
from django.db import models

class BaseOrder(models.Model):
    order_meta = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True
