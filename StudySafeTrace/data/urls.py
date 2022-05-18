from django.urls import path
from data import views

urlpatterns = [
    path('venues', views.venues),
    path('contacts', views.contacts),
    path('vInput', views.vInput),
    path('cInput', views.cInput)
    ]