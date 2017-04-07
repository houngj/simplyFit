from django.test import TestCase
from django.utils import timezone
from .models import utils, workoutLog
from .views import apiUtil
from datetime import date
from django.contrib.auth.models import User
# Create your tests here.
class basicTest(TestCase):
	def test_for_true(self):
		myUtils = utils()
		self.assertIs(myUtils.test(), True)
	'''
	The purpose of this method is to test apiUtil.createUser method.
	The test includes creating the user and then checking if user exists in DB.
	'''
	def test_create_new_user(self):
		apiUtil.createUser("BSly", "Bob@gmail.com", "Sly")
		#userBSly = User.objects.get(userName="BSly")
		userBSly = apiUtil.getUser("BSly")
		self.assertEqual(str(userBSly.username),"BSly")
		self.assertEqual(str(userBSly.email), "Bob@gmail.com")
		userBSly.delete()
		self.assertEqual(None, apiUtil.getUser("BSly"))
	'''
	The purpose of this method is to test apiUtil.createUser method
	The test include creating and existing user and checks if KeyError is raised
	'''
	def test_create_existing_user(self):
		apiUtil.createUser("testCreateExistingUser", "T@gmail.com", "M")
		self.assertRaises(KeyError, apiUtil.createUser, "testCreateExistingUser", "T@gmail.com", "M")
		userTmp = apiUtil.getUser("testCreateExistingUser")
		userTmp.delete()	
		self.assertEqual(None, apiUtil.getUser("testCreateExistingUser"))
	
	'''
	The purpose of this method is to test apiUtil.addDateAndWorkoutHours method.
	The test includes looking up username that exist in the database and also
	usernames that don't exist in the database. 
	'''
	def test_addDateAndWorkoutHours(self):
		apiUtil.createUser("parul", "Parul", "Khullar")

		user_parul = apiUtil.getUser("parul")
		time = date.today()
		
		apiUtil.addDateAndWorkoutHours("parul", time, 2)
		log = apiUtil.getUserWorkOutHoursForDate("parul", time)
		self.assertEqual(str(log.user.username), "parul")
		self.assertEqual(log.date, time)
		self.assertEqual(int(log.hours), 2)

		apiUtil.addDateAndWorkoutHours("parul", time, 2)
		log = apiUtil.getUserWorkOutHoursForDate("parul", time)
		self.assertEqual(str(log.user.username), "parul")
		self.assertEqual(log.date, time)
		self.assertEqual(int(log.hours), 4)
		
		log.delete()
		user_parul.delete()
		
		self.assertEqual(None, apiUtil.getUser("parul"))
		self.assertRaises(KeyError, apiUtil.getUserWorkOutHoursForDate, "parul", time)

	'''
	The purpose of this method is to test apiUtil.updateUserInfo method.
	The test includes creating a user, updating the users information, and then
	confirming that updates were applied
	'''
	def test_updateUserInfo(self):
		apiUtil.createUser("houngj", "sjhoung@gmail.com", "Houng")
		apiUtil.updateUserInfo("houngj", "jerr@gmail.com", "Herng")
		jerrUser = apiUtil.getUser("houngj")
		self.assertEqual(str(jerrUser.email), "jerr@gmail.com")
		self.assertEqual(str(jerrUser.password), "Herng")
		jerrUser.delete()
		self.assertEqual(None, apiUtil.getUser("houngj"))
	
	'''
	The purpose of this method is to test apiUtil.updateUserInfo method.
	The test tries to update a non-existent user which should return a KeyError
	'''
	def test_updateNonExistentUserInfo(self):
		self.assertRaises(KeyError, apiUtil.updateUserInfo, "houngj", "Jerr", "Herng")
	'''
	The purpose of this method is to test apiUtil.deleteLogsByUser method.
	The test includes creating and user and their worklogs, deleting worklogs,
	then checks if there are any worklog entries by the user in DB.
	'''	
	def test_deleteWorkLogByUser(self):
		apiUtil.createUser("houngj", "Joe", "Houng")
		user_joe = apiUtil.getUser("houngj")
		time1 = date(2017,6,24)
		time2 = date(2017,6,25)
		apiUtil.addDateAndWorkoutHours("houngj",time1,2)
		apiUtil.addDateAndWorkoutHours("houngj",time2,2)
		apiUtil.deleteLogsByUser("houngj")
		self.assertEqual(len(workoutLog.objects.filter(user=user_joe)), 0)
		user_joe.delete()
		self.assertEqual(None, apiUtil.getUser("houngj"))
	
	'''
	The purpose of this method is to test apiUtil.deleteUser method.
	The test include creating the user, creating users worklogs, and
	checking if both logs and user is deleted from DB
	'''
	def test_deleteUser(self):
		apiUtil.createUser("houngj", "Joe", "Houng")
		time1 = date(2017,6,24)
		time2 = date(2017,6,25)
		apiUtil.addDateAndWorkoutHours("houngj",time1,2)
		apiUtil.addDateAndWorkoutHours("houngj",time2,2)
		apiUtil.deleteLogsByUser("houngj")
		apiUtil.deleteUser("houngj")
		self.assertEqual(len(workoutLog.objects.filter(user=apiUtil.getUser("houngj"))), 0)
		self.assertEqual(len(User.objects.filter(username="houngj")), 0)
