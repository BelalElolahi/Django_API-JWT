from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, permissions
from .serializer import PhoneSerializer
from .permission import IsOwnerOrReadOnly

# Create your views here.
from .models import Phone
class PhoneList(generics.ListCreateAPIView):
    queryset= Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PhoneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class= PhoneSerializer
    permission_classes = (IsOwnerOrReadOnly,)
