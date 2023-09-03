from django.urls import path

from main import views
from main.apps import MainConfig
from rest_framework.routers import DefaultRouter

from main.views import (WellViewSet, PaymentViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView,
                        LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionCreateAPIView, SubscriptionListAPIView,
                        SubscriptionRetrieveAPIView, SubscriptionUpdateAPIView, SubscriptionDestroyAPIView)

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'well', WellViewSet, basename='well')
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
               path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
               path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
               path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
               path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

               path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription-create'),
               path('subscription/', SubscriptionListAPIView.as_view(), name='subscription-list'),
               path('subscription/<int:pk>/', SubscriptionRetrieveAPIView.as_view(), name='subscription-get'),
               path('subscription/update/<int:pk>/', SubscriptionUpdateAPIView.as_view(), name='subscription-update'),
               path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription-delete')
               ]+router.urls
