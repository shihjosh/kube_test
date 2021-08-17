from django.urls import path
from . import views

urlpatterns = [
    path('', views.core),
    path('other', views.other, name = 'other'),
    path('item1', views.item1, name = 'item1'),
    path('item2', views.item2, name = 'item2'),
]