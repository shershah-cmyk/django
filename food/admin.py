from django.contrib import admin
from .models import ItemModel
# Register your models here.

@admin.register(ItemModel)
class ItemAdmin(admin.ModelAdmin):
    list_display=("item_name","item_desc","item_price")