from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('<str:room>/', views.room,name='room'),
    path('home/checkview',views.checkview,name='checkview'),
    path('send',views.send,name='send'),
    path('getMessage/<str:room>/', views.getMessage,name='getMessage'),
]