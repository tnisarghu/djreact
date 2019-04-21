from rest_framework import routers
from learn.viewsets import LearnViewSet

router = routers.DefaultRouter()

router.register(r'learn', LearnViewSet)