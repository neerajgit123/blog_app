from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
from .models import *


def home(request):
    context = {"title": "Home-Page", "posts": Post.published.all}
    return render(request, "blog_app/home.html", context)


def about(request):
    return render(request, "blog_app/about.html")
