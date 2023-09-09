from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "report"

urlpatterns = [
    path('', views.home, name='home'),
    
    path('single_record/<str:pk>/', views.single_record, name='single_record'),
    
    path('print_record/<str:pk>/', views.print_record, name='print_record'),
    
    path('generat_image/<str:pk>/', views.generat_image, name='generat_image'),
]
