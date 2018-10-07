from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class ContactUs(models.Model):
	name = models.TextField()
	email = models.EmailField()
	#phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	#phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
	phone_number = models.CharField(max_length=17)
	message = models.TextField()
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '%s' % (self.name)
