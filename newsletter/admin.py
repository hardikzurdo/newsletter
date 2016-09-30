from django.contrib import admin

from .forms import SignUpForm 
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	list_display =["__unicode__","timestamp","updated"]
	form = SignUpForm
	# class meta:
	# 	model = SignUp

admin.site.register(SignUp, SignUpAdmin)