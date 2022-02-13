from django.urls import path
from .views import *

urlpatterns = [
    path("home/", home, name="home-view"),
    path("about/", about, name="about-view"),
]
