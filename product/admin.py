from django.contrib import admin
from .models import Category, Tag, Color, Size, City, Province, Product, PropertyRequest, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'updated')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'updated')
    search_fields = ('title',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'color_code', 'timestamp', 'updated')
    search_fields = ('name', 'color_code')

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp', 'updated')
    search_fields = ('name',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp', 'updated')
    search_fields = ('name',)

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp', 'updated')
    search_fields = ('name',)
    filter_horizontal = ('cities',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'category', 'seller', 'is_pub', 'timestamp', 'updated')
    search_fields = ('name', 'description', 'category__title', 'seller__username')
    list_filter = ('category', 'is_pub', 'timestamp', 'updated')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('tags', 'colors', 'favourite')

@admin.register(PropertyRequest)
class PropertyRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'cat', 'is_pub', 'is_available', 'timestamp', 'updated')
    search_fields = ('name', 'description', 'cat__title', 'customer__username')
    list_filter = ('cat', 'is_pub', 'is_available', 'timestamp', 'updated')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('colors',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'product', 'created', 'updated')
    search_fields = ('name', 'email', 'product__name', 'body')
    list_filter = ('created', 'updated')

