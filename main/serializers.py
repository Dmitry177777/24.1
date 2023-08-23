from rest_framework import serializers

from main.models import Well, Lesson


class WellSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lesson.count()

    class Meta:
        model = Well
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'