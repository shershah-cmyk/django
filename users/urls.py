from django.urls import path, include
from . import  views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static  import static
app_name='users'

urlpatterns = [
    path("register/",views.register, name="register"),
    
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    
    path('logout/',authentication_views.LogoutView.as_view(next_page="users:login"),name='logout'),
    path('profile/',views.profiePage,name="profile"),
] +  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
