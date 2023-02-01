from django.urls import path, include
from rest_framework import routers
from .views import StoryViewSet

router = routers.DefaultRouter()
router.register("stories", StoryViewSet, "stories")

urlpatterns = [
    path("", include(router.urls)),
]
