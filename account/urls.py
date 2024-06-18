from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

app_name = 'account'

urlpatterns = [

]
