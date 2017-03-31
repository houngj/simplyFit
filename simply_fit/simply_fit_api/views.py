from django.shortcuts import render
from django.http import HttpResponse
from .models import User
#API utility functions
class apiUtil(object):
	@staticmethod
	def createUser(userName, firstName, lastName):
		user = User(userName=userName, firstName=firstName, lastName=lastName)
		user.save()

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're at simply_fit!")

