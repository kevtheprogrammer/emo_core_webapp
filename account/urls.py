from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'account'

urlpatterns = [
    # path("signup", login_required(SignUpView.as_view()),name="signup"),
]
