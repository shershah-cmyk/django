from django.urls import path, include
from . import  views
from django.contrib.auth import  views as auth_views
app_name='users'

urlpatterns = [
    path("register/",views.register, name="register"),
    
    # path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    
    # path('logout/',authentication_views.LogoutView.as_view(template_name='users/base.html'),name='logout')
    
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
