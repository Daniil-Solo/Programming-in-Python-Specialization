from django.urls import path
from .views import *

urlpatterns = [
    path('echo/', echo),
    path('filter/', filter),
    path('extend/', extend)
]