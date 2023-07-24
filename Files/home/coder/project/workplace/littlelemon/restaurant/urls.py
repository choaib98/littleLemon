# In restaurant/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name="menu"),
]
