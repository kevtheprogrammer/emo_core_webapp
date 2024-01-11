from django.contrib import admin
from django.urls import path

from django.contrib.auth.decorators import login_required

from .views import *

app_name = "product" 

urlpatterns = [
    path('<int:pk>/<str:slug>/', ProductDetailView.as_view(),name="detail"),
    path('favourite/',login_required(FavouriteView.as_view()),name='favourite'),
    path('remove-from-bookmark/<int:pk>/',login_required(FavouriteToggleView.as_view()),name='favourite-toggle'),
    path('advance-search-results/',login_required(product_search),name='advance-search'),
    
    
 
]
