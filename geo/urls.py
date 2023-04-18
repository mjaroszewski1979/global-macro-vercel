from django.urls import path
from . import views

urlpatterns = [
	path('', views.create_user, name='create-user'),
	path('geo-detail/<str:pk>/', views.geo_detail, name='geo-detail'),
	path('geo-create/', views.geo_create, name='geo-create'),
	path('geo-delete/<str:pk>/', views.geo_delete, name='geo-delete'),
]
