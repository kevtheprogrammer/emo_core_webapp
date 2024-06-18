from django.urls import path
from .views import *
from .auth  import  CustomLoginView, CustomTokenRefreshView


urlpatterns = [

    path("login/", CustomLoginView.as_view(), name="access_refresh_token"),
    path("login/refresh/", CustomTokenRefreshView.as_view(), name="refresh_token"),

    #user Urls,
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('products/', ProductViewSet.as_view({'get': 'list', 'post' : 'create'})),
    path('product/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    
    # path('invoices/', InvoiceViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('invoice/<int:pk>/', InvoiceViewSet.as_view({'get': 'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    
    # path('companies/', CompanyViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('company/<int:pk>/', CompanyViewSet.as_view({'get': 'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    
    # path('categories/', CategoryViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put' : 'update', 'delete' : 'destroy'})),

    # path('emails/', EmailingViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('email/<int:pk>/', EmailingViewSet.as_view({'get':'retrieve', 'put' : 'update', 'delete' : 'destroy'})),

    # path('customers/', CustomerViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('customer/<int:pk>/', CustomerViewSet.as_view({'get':'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    
    # path('sales/', SaleViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('sale/<int:pk>/', SaleViewSet.as_view({'get':'retrieve', 'put' : 'update', 'delete' : 'destroy'})),

    # path('tickets/', TicketViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('ticket/<int:pk>/', TicketViewSet.as_view({'get':'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    
    # path('categories/', CategoryViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('category/<int:pk>/', CategoryViewSet.as_view({'get':'retrieve', 'put' : 'update', 'delete' : 'destroy'})),

]      