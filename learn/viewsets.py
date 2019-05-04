from rest_framework import viewsets
from .models import Learn
from  .serializers import LearnSerializer


class LearnViewSet(viewsets.ModelViewSet):
    queryset = Learn.objects.all()
    serializers_class = LearnSerializer
