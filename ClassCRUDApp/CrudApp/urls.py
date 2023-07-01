from django.urls import path
from .views import *

urlpatterns = [
    path('', goHome),

    path('add/', goAdd, name='goAdd'),

    path('update/<int:id>', goUpdate, name='goUpdate'),

    path('delete/<int:id>', goDelete, name='goDelete'),
]
