from rest_framework import viewsets
from .models import Batter, Pitcher
from .serializers import BatterSerializer, PitcherSerializer

class BatterViewSet(viewsets.ModelViewSet):
	queryset = Batter.objects.all()
	serializer_class = BatterSerializer

class PitcherViewSet(viewsets.ModelViewSet):
	queryset = Pitcher.objects.all()
	serializer_class = PitcherSerializer