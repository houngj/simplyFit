from __future__ import unicode_literals

from django.db import models

# Create your models here.
class utils(object):
	def __init__(self):
		self.tmp = None
	def test(self):
		return True


class User(models.Model):
	userName = models.CharField(max_length=50)
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)

class workoutLog(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField('date worked out')
	hours = models.IntegerField(default=0)

