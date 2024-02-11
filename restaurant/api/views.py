from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MenuItem, Order, User
from .serializers import MenuItemSerializer, OrderSerializer, UserSerializer
from django.http import HttpResponse

def index(request):
    
    return HttpResponse("<h1>Взаимодействие с API</h1>\n\
    <h2><a href = 'api/menu-items/'>все позиции меню</a></h2>\n\
    <h2>api/menu-items/id позиции/ - удалить, отредактировать позицию</h2>\n\
    <h2><a href = 'api/orders/'>все заказы</a></h2>\n\
    <h2>api/orders/id заказа/ - отредактировать, удалить заказ</h2>\n\
    <h2><a href = 'api/users/'>все пользователи</a></h2>\n\
    <h2>api/users/id пользователя/ - удалить, отредактировать пользователя</h2>")

class MenuItemListCreate(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrdersByUser(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
    
        user_id = self.kwargs['user_id']
        return Order.objects.filter(user_id=user_id)