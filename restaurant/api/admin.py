from django.contrib import admin
from .models import MenuItem, Order, User
# Register your models here.
@admin.register(MenuItem)
@admin.register(Order)
@admin.register(User)

class PersonAdmin(admin.ModelAdmin):
    pass