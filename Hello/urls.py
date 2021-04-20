"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "krupesh  Admin"
admin.site.site_title = "krupesh Admin Portal"
admin.site.index_title = "Welcome to krupesh Portal"
urlpatterns = [
    path("admin/",admin.site.urls),
    path('data',views.CustomerData),
    path('transfer',views.transfer),
    path('',views.index),
    path('home',views.index),
    path('bankstataement',views.bank),
   
    path('bank_statement_details',views.bank_statement_details),
    path('transfer_hist',views.transfer_money),
    path('home',views.index),
    
]
