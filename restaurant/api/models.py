from django.db import models
from phonenumber_field.phonenumber import PhoneNumber
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    
    # имя пользователя
    firstname = models.CharField(max_length=20)
    
    # фамилия пользователя
    surname = models.CharField(max_length=20)
    
    # номер пользователя
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    
class Dish(models.Model):
    
    # название блюда
    name = models.CharField(max_length=20)
    
    # состав блюда
    composition = models.CharField(max_length=150)

class Order(models.Model):
    
    # пользователь, который сделал заказ
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # содержание заказа
    dishes = models.ManyToManyField(Dish)
    

    
    
    
    
    
    
    
