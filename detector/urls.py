from django.urls import path
from . import views, utilities

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.ai_detector, name='ai_detector'),
    path('get-result/', utilities.get_result, name='get_result')
]

handler404 ='detector.views.page_not_found'
handler500 ='detector.views.server_error'