from django import forms
from .models import ItemModel

class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemModel
        fields = ['item_name','item_desc','item_price','item_image']