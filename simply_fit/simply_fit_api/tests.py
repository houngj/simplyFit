from django.test import TestCase
from django.utils import timezone
from .models import utils, User, workoutLog
from .views import apiUtil
import datetime

# Create your tests here.
class basicTest(TestCase):
	def test_for_true(self):
		myUtils = utils()
		self.assertIs(myUtils.test(), True)
	def test_create_new_user(self):
		apiUtil.createUser("BSly", "Bob", "Sly")
		#userBSly = User.objects.get(userName="BSly")
		userBSly = apiUtil.getUser("BSly")
		self.assertEqual(str(userBSly.userName),"BSly")
		self.assertEqual(str(userBSly.firstName), "Bob")
		self.assertEqual(str(userBSly.lastName), "Sly")
		userBSly.delete()
		self.assertEqual(None, apiUtil.getUser("BSly"))
	def test_create_existing_user(self):
		apiUtil.createUser("testCreateExistingUser", "T", "M")
		self.assertRaises(KeyError, apiUtil.createUser, "testCreateExistingUser", "T", "M")
		userTmp = apiUtil.getUser("testCreateExistingUser")
		userTmp.delete()	
		self.assertEqual(None, apiUtil.getUser("testCreateExistingUser"))
	def test_addDateAndWorkoutHours(self):
		apiUtil.createUser("parul", "Parul", "Khullar")

		user_parul = apiUtil.getUser("parul")
		time = timezone.now()
		apiUtil.addDateAndWorkoutHours("parul", time, 2)

		log = apiUtil.getUserWorkOutHoursForDate("parul", time)
		self.assertEqual(str(log.user.userName), "parul")
		self.assertEqual(log.date, time)
		self.assertEqual(int(log.hours), 2)
		user_parul.delete()
		self.assertEqual(None, apiUtil.getUser("parul"))


