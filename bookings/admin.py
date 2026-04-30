from django.contrib import admin
from .models import Booking, Message, Review
# Register your models here.
admin.site.register(Booking)
admin.site.register(Message)
admin.site.register(Review)