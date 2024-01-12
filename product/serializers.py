from rest_framework import serializers
from .models import Product, Category, Tag, Color, Size, City, Province, PropertyRequst, Review



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['cover','title','timestamp','updated']


class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['name', 'description','price','discount','is_pub','favourite', 'category','author']
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ColorSerializar(serializers.ModelSerializer):
   class Meta:
       model = Color
       fields = '__all__'

class SizeSerializar(serializers.ModelSerializer):
   class Meta:
       model = Size
       fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'
        
class PropertyRequstSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyRequst
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'