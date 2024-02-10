from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    MenuItemListCreate,
    MenuItemRetrieveUpdateDestroy,
    OrderListCreate,
    OrderRetrieveUpdateDestroy,
    UserListCreate,
    UserRetrieveUpdateDestroy,
    OrdersByUser,
)

urlpatterns = [
    path('menu-items/', MenuItemListCreate.as_view(), name='menuitem-list'),
    path('menu-items/<int:pk>/', MenuItemRetrieveUpdateDestroy.as_view(), name='menuitem-detail'),
    path('orders/', OrderListCreate.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroy.as_view(), name='order-detail'),
    path('users/', UserListCreate.as_view(), name='customer-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='customer-detail'),    path('ordersbyuser/<int:user_id>/', OrdersByUser.as_view(), name='ordersbyuser')
]