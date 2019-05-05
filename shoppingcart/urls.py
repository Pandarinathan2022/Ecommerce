from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_home, name='cart'),
    path('update/', views.cart_update, name='cart_update'),
]