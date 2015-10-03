from django.shortcuts import render
from .models import About, Member

def welcome_home(request):
	about = About.objects.all()
	members = Member.objects.all()
	return render(request, 'home/welcome_home.html', {'about': about, 'members': members})
