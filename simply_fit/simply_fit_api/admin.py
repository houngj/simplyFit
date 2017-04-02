from django.contrib import admin

# Register your models here.
from .models import User, workoutLog

admin.site.register(User)
admin.site.register(workoutLog)