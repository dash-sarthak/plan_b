from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("register/", views.register, name="blog-register"),
]
