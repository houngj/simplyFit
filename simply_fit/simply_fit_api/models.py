from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class utils(object):
	def __init__(self):
		self.tmp = None
	def test(self):
		return True

class workoutLog(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField('date worked out')
	hours = models.IntegerField(default=0)

	def __str__(self):
		return self.user.userName
