from django.urls import path
from .views import create_booking, send_message, get_messages

urlpatterns = [
    path('', create_booking),
    path('<int:booking_id>/messages/', get_messages),
    path('<int:booking_id>/messages/send/', send_message),
]