from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.ai_detector, name='ai_detector'),
]

handler404 ='detector.views.page_not_found'
handler500 ='detector.views.server_error'