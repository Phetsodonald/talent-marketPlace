from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_booking(request):
    data = request.data.copy()
    data['organizer'] = request.user.id

    serializer = BookingSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)