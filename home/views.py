from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from . models import Item
from .serializers import ItemSerializer
from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.

class ItemListCreateView(ListCreateAPIView):
    queryset =Item.objects.all()
    serializer_class = ItemSerializer
class ItemDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer