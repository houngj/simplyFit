from django.shortcuts import render
from django.http import HttpResponse
from .models import User
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
# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're at simply_fit!")

