from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView,DestroyAPIView
from . import serializers
from . import models

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):#handles the POST and GET method calls.
    queryset=models.Menu.objects.all()
    serializer_class=serializers.MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):#processing GET, PUT and DELETE method calls.
    queryset=models.Menu.objects.all()
    serializer_class=serializers.MenuSerializer