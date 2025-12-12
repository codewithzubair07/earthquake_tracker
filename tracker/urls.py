from django.urls import path
from . import views

urlpatterns = [
    path('', views.earthquake_list, name='earthquake_list'),
]
