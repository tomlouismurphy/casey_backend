from django.db import models
from django.utils import timezone

class Batter(models.Model):
	name = models.CharField(max_length=50)
	position = models.CharField(blank=True, null=True, max_length=50)
	plate_appearances = models.IntegerField(default=0)
	at_bats = models.IntegerField(default=0)
	hits = models.IntegerField(default=0)
	walks = models.IntegerField(default=0)
	hit_by_pitch = models.IntegerField(default=0)
	sacrifice_flies = models.IntegerField(default=0) 
	sacrifice_hits = models.IntegerField(default=0)
	singles = models.IntegerField(default=0)
	doubles = models.IntegerField(default=0)
	triples = models.IntegerField(default=0)
	home_runs = models.IntegerField(default=0)
	def __str__(self):
		return self.name

class Pitcher(models.Model):
	name = models.CharField(max_length=50)
	batters_faced = models.IntegerField(default=0)
	hits_allowed = models.IntegerField(default=0)
	walks_allowed = models.IntegerField(default=0)
	hit_by_pitches_allowed = models.IntegerField(default=0)
	home_runs_allowed = models.IntegerField(default=0)
	def __str__(self):
		return self.name