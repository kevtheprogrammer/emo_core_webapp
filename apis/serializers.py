from rest_framework import serializers
from account.models import User
from product.models import Product
from booking.models import Events
from product.models import Category, Tag, Color, Size, City, Province, Product, PropertyRequest, Review
# from emailing.models import Emailing
# from tickets.models import Ticket
# from sales_market.models import Customer, Sale
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


# user serializers

class UserSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.name', required=False)

    class Meta:
        model = User
        fields = [
            'id', 'avatar', 'email', 'email_confirmed', 'access_code', 'first_name',
            'last_name', 'dob', 'nrc', 'country', 'phone', 'is_staff', 'location',
            'date_joined', 'is_active', 'is_verified', 'creation_ip_address',
            'deletion_ip_address'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.country:
            representation['country'] = instance.country.name
        return representation
    
class UploadCSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['users_csv']


# Product Users       

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['thumb', 'name', 'description', 'price', 'discount', 'is_pub', 'favourite', 'category', 'img']
        
# class InvoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Invoice
#         fields = ['customer', 'company', 'product', 'invoice_number', 'location']
        
# class CompanySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = ['business_name', 'business_email', 'business_phone_number']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['cover', 'title']

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['title', 'barner', 'start_date', 'end_date', 'img', 'img2', 'price', 'location','description']

# email serializers
        
# class EmailingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Emailing
#         fields = ['to_address', 'cc_address', 'bcc_address', 'body', 'attachment']


# #invoice
    
# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['first_name', 'last_name', 'email', 'phonenumber', 'address']
        
# class SaleSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Sale
#         fields = ['product', 'customer', 'quantity', 'unity_price', 'total_amount']

# #tickets

# class TicketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ticket
#         fields = ['cat', 'description',  'status', 'client_phonenumber' ,'crm_manager']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'cover', 'title', 'timestamp', 'updated', 'slug']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title', 'timestamp', 'updated']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'color_code', 'timestamp', 'updated']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name', 'timestamp', 'updated']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'timestamp', 'updated']

class ProvinceSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Province
        fields = ['id', 'name', 'cities', 'timestamp', 'updated']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    seller = serializers.StringRelatedField(read_only=True)
    location_city = CitySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    colors = ColorSerializer(many=True, read_only=True)
    favourite = serializers.StringRelatedField(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'thumb', 'name', 'description', 'price', 'latitude', 
            'longitude', 'location_city', 'discount', 'category', 
            'seller', 'img1', 'img2', 'img3', 'tags', 'colors', 'favourite', 
            'is_pub', 'avr_views_duration', 'views', 'creation_ip_address', 
            'deletion_ip_address', 'updated', 'timestamp', 'slug', 'author'
        ]
class ProductCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'thumb', 'name', 'description', 'price', 'location_city', 'discount', 'category', 
            'img1', 'img2', 'img3', 'tags', 'colors', 
            'is_pub', 'creation_ip_address', 
            'deletion_ip_address']
        

class PropertyRequestSerializer(serializers.ModelSerializer):
    cat = CategorySerializer(read_only=True)
    colors = ColorSerializer(many=True, read_only=True)
    customer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PropertyRequest
        fields = [
            'id', 'thumb', 'name', 'description', 'cat', 'img1', 'img2', 
            'img3', 'colors', 'is_pub', 'is_available', 'avr_views_duration', 
            'views', 'updated', 'timestamp', 'slug', 'customer'
        ]

class ReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'name', 'email', 'body', 'product', 'created', 'updated']
