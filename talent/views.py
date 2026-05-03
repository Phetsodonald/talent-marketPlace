from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TalentProfile
from .serializers import TalentProfileSerializer

# Create your views here.
@api_view(['GET'])
def get_talents(request):
    talents = TalentProfile.objects.all()
    serializer = TalentProfileSerializer(talents, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_talent(request):
    try:
        talent = TalentProfile.objects.get(slug=slug)
        serializer = TalentProfileSerializer(talent)
        return Response(serializer.data)
    except TalentProfile.DoesNotExist:
        return Response({"error": "Talent not found"}, status=404)