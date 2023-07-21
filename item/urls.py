from django.urls import path
from item.views import ItemView, CategoryListCreateView

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
]