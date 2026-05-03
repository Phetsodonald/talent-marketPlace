from rest_framework import serializers
from .models import TalentProfile, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TalentProfileSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = TalentProfile
        fields = '__all__'