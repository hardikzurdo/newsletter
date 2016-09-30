from django.shortcuts import render
from .forms import ContactForm, SignUpForm
def home(request):
	title = "Welcome"
	form = SignUpForm(request.POST or None)
	
	context = {
		"title": title,
		"form": form
		}

	
	if form.is_valid():

		instance = form.save(commit = False)
		if not instance.full_name:
			instance.full_name = "Hardik"
		instance.save()
		context = {
		"title": "Thank you"
		}
		
	return render(request,"home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	
	context ={
		"form": form
	}
	return render(request,"forms.html", context)

	