from main.apps import MainConfig
from rest_framework.routers import DefaultRouter

from main.views import WellViewSet

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'well', WellViewSet, basename='well' )


urlpatterns = [

] + router.urls