from django.urls import path
from .views import *

urlpatterns = [
    
    

    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('product/<int:pk>', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete' : 'destroy'})),
    
    path('categories/', CategoryViewSet.as_view({'get': 'list' })),
    path('category/<int:pk>', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete' : 'destroy'})),
    
    path('tags/', TagViewSet.as_view({'get': 'list' })),
    path('tag/<int:pk>', TagViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete' : 'destroy'})),
    
    path('colors/', ColorViewSet.as_view({'get': 'list' })),
    path('color/<int:pk>', ColorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete' : 'destroy'})),
    
    path('sizes/', SizeViewSet.as_view({'get': 'list' })),
    path('size/<int:pk>', SizeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete' : 'destroy'})),
    
    path('cities/', CityViewSet.as_view({'get': 'list' })),
    path('city/<int:pk>', CityViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete' : 'destroy'})),
    
    path('provinces/', ProvinceViewSet.as_view({'get': 'list' })),
    path('province/<int:pk>', ProvinceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete' : 'destroy'})),
    
    path('properties', PropertyRequestViewSet.as_view({'get': 'list' })),
    path('property/<int:pk>', PropertyRequestViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete' : 'destroy'})),
    
    path('reviews', ReviewViewSet.as_view({'get': 'list' })),
    path('review/<int:pk>', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete' : 'destroy'})),
    
    path('vehicles/', VehicleViewSet.as_view({'get': 'list','post': 'create' })),
    path('vehicle/<int:pk>', VehicleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete' : 'destroy'})),
]
