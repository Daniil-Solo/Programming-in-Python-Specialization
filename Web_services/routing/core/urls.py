from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('simple_route/', simple_route),
    path('slug_route/<slug:slug_content>/', slug_route),
    path('sum_route/<int:num1>/<int:num2>/', sum_route),
    path('sum_get_method/', sum_get_method),
    path('sum_post_method/', sum_post_method)
]