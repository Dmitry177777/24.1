
from rest_framework import viewsets, generics, routers
from rest_framework.filters import SearchFilter, OrderingFilter
from django.urls import path, include
from rest_framework.permissions import IsAuthenticated, AllowAny

from main.models import Well, Lesson, Payment, Subscription
from rest_framework.response import Response

from main.paginators import MainPaginator
from main.permissions import IsLessonOwner, IsModerator
from main.serializers import WellSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer
from django.shortcuts import get_object_or_404

from users.models import UserRoles


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['well_name', 'payment_method']
    ordering_fields = ['date_of_payment']
    permission_classes = [IsAuthenticated]



class WellViewSet(viewsets.ModelViewSet):
    serializer_class = WellSerializer
    queryset = Well.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MainPaginator


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]




class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    # queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsLessonOwner]
    pagination_class = MainPaginator

    def get_queryset (self):
        user=self.request.user
        role=self.request.user.role
        if role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsLessonOwner]



class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsLessonOwner]
class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsLessonOwner]




class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsLessonOwner]

    def get_queryset (self):
        user=self.request.user
        role=self.request.user.role
        if role == UserRoles.MODERATOR:
            return Subscription.objects.all()
        else:
            return Subscription.objects.filter(owner=user)


class SubscriptionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsLessonOwner]



class SubscriptionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsLessonOwner]
class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated, IsLessonOwner]