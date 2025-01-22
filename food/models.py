from django.db import models

# Create your models here.
class ItemModel(models.Model):
    item_name = models.CharField(max_length=255)
    item_desc = models.CharField(max_length=255)
    item_price = models.IntegerField()