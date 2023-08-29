
from rest_framework import viewsets, generics, routers
from django.urls import path, include
from main.models import Well, Lesson
from rest_framework.response import Response
from main.serializers import WellSerializer, LessonSerializer
from django.shortcuts import get_object_or_404


class WellViewSet(viewsets.ModelViewSet):
    serializer_class = WellSerializer
    queryset = Well.objects.all()

    # def list(self, request):
    #     # Метод для вывода списка курсов с определением выборки из базы и указанием сериализатора
    #     queryset = Well.objects.all()
    #     serializer = WellSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     # Метод для вывода информации по курсу с определением выборки из базы и указанием сериализатора
    #     queryset = Well.objects.all()
    #     well = get_object_or_404(queryset, pk=pk)
    #     serializer = WellSerializer(well)
    #     return Response(serializer.data)

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()