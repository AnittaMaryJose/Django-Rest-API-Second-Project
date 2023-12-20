from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from . models import Item
from .serializers import ItemSerializer






# Create your views here.

class ItemListCreateView(ListCreateAPIView):
    queryset =Item.objects.all()
    serializer_class = ItemSerializer
