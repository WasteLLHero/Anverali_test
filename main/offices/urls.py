
from django.contrib import admin
from django.urls import include, path
from .views import MainView, OrderListView

urlpatterns = [
    path('main/', MainView.as_view()),    
    path('orders/', OrderListView.as_view())
]
