from rest_framework import serializers
from .models import Family

class FamilySerializers(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = (
            'name', 'phone_number'
        )