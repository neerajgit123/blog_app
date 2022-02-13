from django.urls import path
from .views import *

urlpatterns = [
    path("register/", userregister, name="register-view"),
    path('login/',userlogin,name='login-view'),
]
