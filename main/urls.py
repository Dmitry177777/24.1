from django.urls import path

from main import views
from main.apps import MainConfig
from rest_framework.routers import DefaultRouter

from main.views import WellViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'well', WellViewSet, basename='well')



urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

                  # path('well/create/', WellCreateAPIView.as_view(), name='lesson-create'),
                  # path('well/', WellListAPIView.as_view(), name='lesson-list'),
                  # path('well/<int:pk>/', WellRetrieveAPIView.as_view(), name='lesson-get'),
                  # path('well/update/<int:pk>/', WellUpdateAPIView.as_view(), name='lesson-update'),
                  # path('well/delete/<int:pk>/', WellDestroyAPIView.as_view(), name='lesson-delete'),



              ] + router.urls
