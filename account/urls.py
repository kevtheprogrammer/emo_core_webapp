from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import AuthTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

app_name = 'account'

urlpatterns = [

    path("login/", AuthTokenObtainPairView.as_view(), name="access_refresh_token"),
    path("login/refresh/", AuthTokenObtainPairView.as_view(), name="refresh_token"),

    path("signup/", SignupView.as_view(), name="signup"),

    path("users/", UserViewSet.as_view({'get' : 'list'})),
    path("user/<int:pk>/", UserViewSet.as_view({'get' : 'retrieve', 'put' : 'update', 'delete' : 'destroy'})),



]
