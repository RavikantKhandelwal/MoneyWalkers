from django.shortcuts import render
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from .models import *


@csrf_exempt
def home_page(request, template="home/home_page.html"):
	if request.method == "POST":
		name = request.POST.get('name')
		phone_number = request.POST.get('phone_number')
		email = request.POST.get('email')
		message = request.POST.get('message')
		ContactUs.objects.create(name=name,phone_number= phone_number, email=email, message=message)
	context = {}
	return render(request, template, context)
