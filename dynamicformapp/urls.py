# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_item/', views.add_item, name='add_item'),
    path('item_list/', views.item_list, name='item_list'),


]
