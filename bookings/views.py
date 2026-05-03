from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Booking, Message
from .serializers import BookingSerializer, MessageSerializer


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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        return Response({"error": "Booking not found"}, status=404)

    # 🔐 Only participants can send messages
    if request.user != booking.organizer and request.user != booking.talent.user:
        return Response({"error": "Not allowed"}, status=403)

    message = Message.objects.create(
        booking=booking,
        sender=request.user,
        text=request.data.get('text')
    )

    serializer = MessageSerializer(message)
    return Response(serializer.data, status=201)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_messages(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        return Response({"error": "Booking not found"}, status=404)

    # 🔐 Only participants can view
    if request.user != booking.organizer and request.user != booking.talent.user:
        return Response({"error": "Not allowed"}, status=403)

    messages = booking.messages.all().order_by('created_at')
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)