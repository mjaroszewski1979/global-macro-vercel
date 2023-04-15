from django.urls import path, include
from django.contrib.auth.views import LogoutView

from . import views, htmx_views


urlpatterns = [
 
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("cars/", views.CarList.as_view(), name="car_list"),
    path('accounts/', include('allauth.urls') ),
]

htmx_url_patterns = [
    path("check-username/", htmx_views.check_username, name='check-username'),
    path('add-car/', htmx_views.add_car, name='add_car'),
    path('delete-car/<int:id>/', htmx_views.delete_car, name='delete_car'),
    path('search-car/', htmx_views.search_car, name='search_car'),
    path('clear/', htmx_views.clear, name='clear'),
    path('sort/', htmx_views.sort, name='sort'),
    path('detail/<int:id>/', htmx_views.detail, name='detail'),
    path('car-list-partial', htmx_views.cars_partial, name='car_list_partial'),
    path('upload-photo/<int:id>/', htmx_views.upload_photo, name='upload_photo'),
]

urlpatterns += htmx_url_patterns
