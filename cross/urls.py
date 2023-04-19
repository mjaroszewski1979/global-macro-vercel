from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('gold.urls')),
    path('admin/', admin.site.urls),
] 
