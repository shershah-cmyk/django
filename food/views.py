from django.shortcuts import  render
from django.http  import HttpResponse
from .models import ItemModel
# Create your views here.

def index(request):
    item_list = ItemModel.objects.all()
    context = {
        'items':item_list
    }
    return render (request,'food/index.html',context)
    
def detail(request,item_id):
    item=ItemModel.objects.get(pk=item_id)
    context={
        'item':item
    }
    return render(request ,'food/detail.html',context)