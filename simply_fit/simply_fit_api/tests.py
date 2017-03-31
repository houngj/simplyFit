from django.test import TestCase
from .models import utils, User
from .views import apiUtil
# Create your tests here.
class basicTest(TestCase):
	def test_for_true(self):
		myUtils = utils()
		self.assertIs(myUtils.test(), True)
	def test_create_new_user(self):
		apiUtil.createUser("BSly", "Bob", "Sly")
		userBSly = User.objects.get(userName="BSly")
		
		self.assertEqual(str(userBSly.userName),"BSly")
		self.assertEqual(str(userBSly.firstName), "Bob")
		self.assertEqual(str(userBSly.lastName), "Sly")
		
		
