from django.urls import path
from .views import *

urlpatterns = [
    path('table/', table),
    path('', home),
    path('table/<int:pk>/', jewelry)
]
