from django.contrib import admin
from .models import *


class ContactUsModelAdmin(admin.ModelAdmin):
	list_display = ["name", "email", "phone_number", "message", "created"]

	class Meta:
		model = ContactUs


admin.site.register(ContactUs, ContactUsModelAdmin)