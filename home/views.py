from django.shortcuts import render
from .models import About

def welcome_home(request):
	about = About.objects.all()
	return render(request, 'home/welcome_home.html', {'about': about})
