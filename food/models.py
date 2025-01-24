from django.db import models

# Create your models here.
class ItemModel(models.Model):
    item_name = models.CharField(max_length=255)
    item_desc = models.CharField(max_length=255)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT27gTKHqKhHk3i-EiarE5Q9IND_awvKaKjxw&s")