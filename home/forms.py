from django import forms
from .models import ContactUs
from django.forms import ModelForm


class ContactUsModelForm(ModelForm):
	class Meta:
		model = ContactUs
		fields = {'name', 'email', 'phone_number', 'message'}
