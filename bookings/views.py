from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Booking
from .serializers import BookingSerializer

# Create your views here.
@api_view(['POST'])
def create_booking(request):
    serializer = BookingSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=400)