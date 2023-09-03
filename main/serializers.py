from django.core.serializers import serialize
from django.http import JsonResponse
from rest_framework import serializers
import json

from main.models import Well, Lesson, Payment, Subscription
from main.validators import lesson_linkValidator
from users.models import UserRoles


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ["id", "lesson_name", "lesson_description", "lesson_link", "well_name"]
        validators = [lesson_linkValidator(field='lesson_link')]



class PaymentSerializer(serializers.ModelSerializer):
     class Meta:
        model = Payment
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'




class WellSerializer(serializers.ModelSerializer):
    subscription = serializers.SerializerMethodField()
    # subscription = serializers.BooleanField(read_only=True, source='subscription_set.last.is_activ')
    lesson_count = serializers.SerializerMethodField()
    # lesson = LessonSerializer(many=True, read_only=True, source='lesson_set')
    lesson = serializers.SerializerMethodField()





    class Meta:
        model = Well
        fields = '__all__'



    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    def get_lesson(self, instance):
        user = self.context['request'].user
        role = self.context['request'].user.role
        if role == UserRoles.MODERATOR:
            # Получаем сет объектов QuerySet
            response = instance.lesson_set.all()
            # Сериализуем объкты QuerySet в формат Json
            serialized_data = serialize("json", response, use_natural_foreign_keys=True)
            serialized_data = json.loads(serialized_data)
            return serialized_data
        else:
            #Получаем сет объектов QuerySet
            response = instance.lesson_set.filter(owner=user).all()
            #Сериализуем объкты QuerySet в формат Json
            serialized_data = serialize("json", response, use_natural_foreign_keys=True)
            serialized_data = json.loads(serialized_data)

           return serialized_data

    def get_subscription(self, instance):
        user = self.context['request'].user
        for i in instance.subscription_set.all():
            if i.owner == user:
                return i.is_activ







