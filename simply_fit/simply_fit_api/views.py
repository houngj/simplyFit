from django.shortcuts import render
from django.http import HttpResponse
from .models import User, workoutLog

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

	''' 
	The purpose of this method is to add date and hours for a specific user. 
	@param user=string
		   date=django.util.timezeon
		   hours=int
	@return 
			"success" : if the user was exist
			error: if the user does not exist
	'''
	@staticmethod
	def addDateAndWorkoutHours(user, date, hours):
		if(apiUtil.getUser(user) != None):
			userToUpdate = apiUtil.getUser(user)
			totalHours = hours
			try:
				log = workoutLog.objects.get(user=userToUpdate, date=date)
				totalHours += log.hours
				log.delete()
			except:
				None

			updateLog = workoutLog(user=userToUpdate, date=date, hours=totalHours)
			updateLog.save()

		else:
			raise KeyError("User does not exist! Please add user first")

	'''
	The purpose of this method is to retreive workout log 
	@param user=string
		   date=django.util.timezone

	@return 
		log = (user, date, hours)
		error: if the user doesn't exist
	'''
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
	'''
	The purpose of this method is to update a users information.
	@param  user=string
		new_firstName=string
		new_lastName=string
		
	@return
		None
	'''
	@staticmethod
	def updateUserInfo(user, new_firstName=None, new_lastName=None):
		updateUser = apiUtil.getUser(user)
		if updateUser != None:
			if new_firstName != None:
				updateUser.firstName=new_firstName
			if new_lastName != None:
				updateUser.lastName=new_lastName
			updateUser.save()
			return "Success"
		else:
			raise KeyError("User does not exist, update failed")
        '''
	The purpose of this method is to delete worklogs by user name
        @param user=string

        @return
                None
        '''	
	@staticmethod
        def deleteLogsByUser(user):
                targetUser = apiUtil.getUser(user)
                if targetUser != None:
                        workoutLog.objects.filter(user=targetUser).delete()
                else:
                        None
	'''
        The purpose of this method is to delete user and worklogs by user name
        @param user=string

        @return
                None
        '''
	@staticmethod
	def deleteUser(user):
		if apiUtil.getUser(user) != None:
			apiUtil.deleteLogsByUser(user)
			apiUtil.getUser(user).delete()
		else:
			None

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're at simply_fit!")

