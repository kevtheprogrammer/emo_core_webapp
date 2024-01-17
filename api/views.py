from django.shortcuts import render

# views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status , viewsets
from account.models import User
from account.serializers import UserListSerializer
from product.models import *
from product.serializers import *
from product.serializers import *
from django.shortcuts import get_object_or_404
# viewsets endepoins for the apis

# @permission_classes([IsAuthenticated])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
@permission_classes([IsAuthenticated])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
@permission_classes([IsAuthenticated])
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

@permission_classes([IsAuthenticated])
class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializar

@permission_classes([IsAuthenticated])   
class SizeViewSet(viewsets.ModelViewSet): 
    queryset = Size.objects.all()
    serializer_class = SizeSerializar
 
@permission_classes([IsAuthenticated])  
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

@permission_classes([IsAuthenticated])   
class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

@permission_classes([IsAuthenticated])  
class PropertyRequestViewSet(viewsets.ModelViewSet):
    queryset = PropertyRequst.objects.all()
    serializer_class = PropertyRequstSerializer  

@permission_classes([IsAuthenticated])
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer