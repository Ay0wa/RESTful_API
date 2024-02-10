# restaurant_app/serializers.py

from rest_framework import serializers
from .models import MenuItem, Order, User

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price']
        
class OrderSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'items', 'status', 'user']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone_number']