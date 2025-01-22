from django.urls import path
from . import views 
app_name='food'
urlpatterns = [
    path('',views.index, name="home"),
    path('<int:item_id>/',views.detail,name='detail'),
]
