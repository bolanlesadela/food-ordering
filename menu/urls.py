from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('order/<int:item_id>/', views.place_order, name='place_order'),
    path('orders/', views.orders, name='orders'),
    path('orders/update/<int:order_id>/', views.update_status, name='update_status'),
]