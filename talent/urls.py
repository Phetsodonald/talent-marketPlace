from django.urls import path
from .views import get_talents, get_talent

urlpatterns = [
    path('', get_talents),
    path('<slug:slug>/', get_talent),
]