# from django.contrib import admin


# from .models import *

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ( 'title', 'updated', )
#     search_fields = ( 'title', )


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'discount','description',  )
#     search_fields = ('name', 'price', 'description' ,)
#     list_filter = ('category', 'author__email','price','updated',)


#     actions = [ 'publish', 'draft' ]

#     def publish(self, queryset):
#         queryset.update(is_pub=True)

#     def draft(self, queryset):
#         queryset.update(is_pub=False)


# @admin.register(Region)
# class RegionAdmin(admin.ModelAdmin):
#     list_display = ( 'name', )
#     list_filter = ('updated',)


# # @admin.register(Order)
# # class OrderAdmin(admin.ModelAdmin):
# #     list_display = ( 'status', 'client','ordered','shipping_fee', )
# #     search_fields = ( 'client.email', )
# #     list_filter = ('updated','status')

# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ( 'title', 'timestamp', )
#     search_fields = ( 'title', )

from django.contrib import admin
from .models import Category, Tag, Color, Size, City, Province, Product, PropertyRequst, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated']
    # Add other configurations if needed

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated']
    # Add other configurations if needed

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'color_code', 'timestamp', 'updated']
    # Add other configurations if needed

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp', 'updated']
    # Add other configurations if needed

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp', 'updated']
    # Add other configurations if needed

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp', 'updated']
    # Add other configurations if needed

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'seller', 'is_pub', 'timestamp', 'updated']
    # Add other configurations if needed

@admin.register(PropertyRequst)
class PropertyRequstAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_pub', 'is_available', 'timestamp', 'updated']
    # Add other configurations if needed

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'product', 'created', 'updated']
    # Add other configurations if needed
