"""
Custom user routes and endpoints
"""
from django.urls import path
from .views import home, blog, adv_1


urlpatterns = [
    path("", home, name="home"),
    path("blog/", blog, name="blog"),
    path("adv1/", adv_1, name="adv_1"),
]
