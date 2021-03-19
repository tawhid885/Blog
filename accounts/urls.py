from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),    
    path('register/',views.register, name='register'),
    path('accounts/profile/', views.profile, name = 'profile'),
    path('login/',auth_views.LoginView.as_view(template_name ='accounts/login.html'), name ='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name ='accounts/logout.html'), name ='logout'),
    
]