from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=256)
    category = models.CharField(max_length=64)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.name} [{self.category}] Stored:[{self.amount}]"
