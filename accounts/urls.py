from django.urls import path
from . import views

urlpatterns = [
    path('registerUser/', views.register_user, name='registerUser'),
]