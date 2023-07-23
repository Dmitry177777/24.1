from django.shortcuts import render
from rest_framework import viewsets
from main.models import Well
from main.serliazers import WellSeializer


class WellVieSet(viewsets.ModelViewSet):
    serializer_class = WellSeializer
    queryset = Well.objects.all()


# Create your views here.
