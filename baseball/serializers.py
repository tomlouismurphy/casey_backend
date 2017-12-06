from rest_framework import serializers
from .models import Batter, Pitcher

class BatterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Batter
		fields = ("name", "position", "plate_appearances", "at_bats", "hits", "walks", "hit_by_pitch", "sacrifice_flies", "sacrifice_hits", "singles", "doubles", "triples", "home_runs")

class PitcherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pitcher
		fields = ("name", "batters_faced", "hits_allowed", "walks_allowed", "hit_by_pitches_allowed", "home_runs_allowed")