
from django.contrib import admin
from django.urls import include, path
from .views import CreateOrderView, ExecutorOrderListView, OrderListView, OrderPersonalListView

urlpatterns = [
    path('', OrderListView.as_view()),    
    path('orders/', OrderListView.as_view(), name='orders_all'),
    path('orders/create/', CreateOrderView.as_view(), name='post_orders'),
    path('orders/personal/', OrderPersonalListView.as_view(), name='my_orders'),
    path('orders/executor/', ExecutorOrderListView.as_view(), name='executor_orders'),
]
