from django.shortcuts import render
from django.http import HttpResponse
from .models import User, workoutLog
import datetime
#API utility functions
class apiUtil(object):

	@staticmethod
	def createUser(userName, firstName, lastName):
		if apiUtil.getUser(userName) == None:
			user = User(userName=userName, firstName=firstName, lastName=lastName)
			user.save()
			return "Success"
		else:
			raise KeyError("User exists, please use a different username")
	
	@staticmethod
	def getUser(user):
		try:
			user = User.objects.get(userName=user)
			return user
		except:
			return None

	''' This method add the date and workout hours for a specified user
		addDateAndWorkoutHours:
			@params : username: [username; firstName; lastName]
					  date: dateTime
					  Hours: integer
	'''
	@staticmethod
	def addDateAndWorkoutHours(user, date, hours):
		if(apiUtil.getUser(user) != None):
			userToUpdate = apiUtil.getUser(user)
			log = workoutLog(user=userToUpdate, date=date, hours=hours)
			log.save()
			return "Success"
		else:
			raise KeyError("User does not exist! Please add user first")

	@staticmethod
	def getUserWorkOutHoursForDate(user, date):
		if(apiUtil.getUser(user) != None):
			sqlUser = apiUtil.getUser(user)
			try:
				log = workoutLog.objects.get(user=sqlUser, date=date)
				return log
			except:
				log = workoutLog(user=sqlUser, date=date, hours=0)
				return log
		else:
			raise KeyError("User does not exist! Please add User first")


# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're at simply_fit!")

