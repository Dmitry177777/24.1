from rest_framework import serializers

from main.models import Well, Lesson, Payment
from main.validators import lesson_linkValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ["id", "lesson_name", "lesson_description", "lesson_link", "well_name"]
        validators = [lesson_linkValidator(field='lesson_link')]



class PaymentSerializer(serializers.ModelSerializer):
     class Meta:
        model = Payment
        fields = '__all__'


class WellSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True, source='lesson.queryset')


    class Meta:
        model = Well
        fields = '__all__'

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

