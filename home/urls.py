from django.urls import path
from . views import ItemListCreateView,ItemDetailAPIView

urlpatterns = [
    path('', ItemListCreateView.as_view(),name='listcreate'), 
    path('items/<pk>/', ItemDetailAPIView.as_view(), name='list'),
]