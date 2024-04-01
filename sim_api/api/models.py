from django.db import models
import datetime

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=64)
    quantity = models.IntegerField()

    price = models.FloatField(
        null=True,
        blank=True
        )

    manufacturer = models.CharField(
        null=True,
        blank=True,
        max_length=128
        )

    stock = models.BooleanField(
        default=True
    )

    description = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        )

    def __str__(self):
        return f"{self.name} [{self.category}] Stored:[{self.quantity}]"
