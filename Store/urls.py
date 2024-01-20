"""
URL configuration for TechStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import include, path
from Store import views
urlpatterns = [
    path('', views.Home, name='Home'),
    
    path('Administration', views.Admin, name='Administration'),
    
    path('SignupHandler', views.SignupHandler, name='SignupHandler'),
    
    path('Auth', views.Auth, name='Auth'),
    
    path('Login', views.Login, name='Login'),
    
    path('Register', views.Register, name='Register'),
    
    path('ApiProducts', views.Api_Products_Info, name='ApiProducts'),
    
    path('AddProduct', views.AddProduct, name='AddProduct'),
    
    
    path('UserDelete', views.UserDelete , name='UserDelete'),

    path('Logout', views.Logout , name='Logout'),
]
