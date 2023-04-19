# Django imports
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

# App imports
from . import views


urlpatterns = [
 
    path('search/', views.SearchView.as_view(), name='search'),
    path('', views.HomeView.as_view(), name='home'),
    path('long/', TemplateView.as_view(template_name='long.html'), name='long'),
    path('sharpe/', TemplateView.as_view(template_name='sharpe.html'), name='sharpe'),
    path('cagr/', TemplateView.as_view(template_name='cagr.html'), name='cagr'),
    path('strategies_create/', views.StrategiesCreate.as_view(), name='strategies_create'),
    path('strategies_update/<slug:slug>/', views.StrategiesUpdate.as_view(), name='strategies_update'),
    path('strategies_delete/<slug:slug>/', views.StrategiesDelete.as_view(), name='strategies_delete'),
    path('strategies_list/', views.StrategiesList.as_view(), name='strategies_list'),
    path('strategies_list/<slug:slug>/', views.StrategiesDetail.as_view(), name='strategies_detail'),
    path('strategy_detail/<slug:slug>/', views.StrategyView.as_view(), name='strategy_detail'),
    path('market_detail/<slug:slug>/', views.MarketDetail.as_view(), name='market_detail'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
 
]

handler404 ='catalog.views.page_not_found'
handler500 ='catalog.views.server_error'