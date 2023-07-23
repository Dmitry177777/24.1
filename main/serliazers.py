from rest_framework import serializers

from main.models import Well


class WellSeializer(serializers.ModelSerializer):

    class Meta:
        model = Well
        fields = '__all__'