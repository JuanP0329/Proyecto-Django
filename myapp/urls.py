from django.urls import path
from .views import hello, about, index

urlpatterns = [
    path('', index),
    path('about', about),
    path('hello/<str:username>', hello),
]
