from django.urls import path

from . import views

app_name='avail_management'
urlpatterns = [
    path('orders', views.list_order, name='orders'),
]