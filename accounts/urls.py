from django.urls import path
from . import views

urlpatterns = [
    path('registerUser/', views.register_user, name='registerUser'),
    path('registerVendor/', views.register_vendor, name='registerVendor'),
]