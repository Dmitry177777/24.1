from django.shortcuts import render
from rest_framework import viewsets
from main.models import Well
from main.serliazers import WellSerializer


class WellViewSet(viewsets.ModelViewSet):
    serializer_class = WellSerializer
    queryset = Well.objects.all()


# Create your views here.
