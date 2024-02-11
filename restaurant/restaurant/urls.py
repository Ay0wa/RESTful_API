from django.contrib import admin
from django.urls import path, include
from api.views import index
urlpatterns = [
    path('', index, name="home"),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]