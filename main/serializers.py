from rest_framework import serializers

from main.models import Well, Lesson


class WellSerializer(serializers.ModelSerializer):
    # lesson_count = serializers.IntegerField(source='lesson_set.count()', default=0, read_only=True)
    lesson_count = serializers.SerializerMethodField()

    class Meta:
        model = Well
        fields = '__all__'

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'