from django.urls import path
from . import views

urlpatterns = [
    path('', views.core),
    path('other', views.other),
]