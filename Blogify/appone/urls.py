from django.urls import path
from . import views

urlpatterns = [
    path("blogs", views.showblogs, name="blogsurl"),
    path("", views.showhome, name="homeurl")
]